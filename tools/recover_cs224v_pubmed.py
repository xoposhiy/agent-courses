"""Register the verified Europe PMC full text for a course-linked PubMed source."""

import json
from pathlib import Path
from urllib.parse import urlencode

from corpus import Corpus, code_block
from collect_stanford_cs224v import BASE, DOC_URL
from finish_stanford_cs224v import add_snapshot
from qa_stanford_cs224v import update_core_links


def main():
    corpus = Corpus("courses/stanford-cs224v", "stanford-cs224v", "Stanford CS224V: Agentic AI", BASE)
    metadata_path = corpus.root / "raw" / "metadata" / "pubmed-39954218-europepmc.json"
    response = json.loads(metadata_path.read_text(encoding="utf-8"))
    if response.get("hitCount") != 1:
        raise ValueError("The targeted PubMed lookup did not return exactly one work")
    article = response["resultList"]["result"][0]
    parsed = json.loads((corpus.root / "raw" / "metadata" / "pmc-13346298-parsed.json").read_text(encoding="utf-8"))
    if not parsed.get("full_text_available"):
        raise ValueError("JATS verification did not find a full article body")
    item = corpus.add("https://europepmc.org/articles/PMC13346298?pdf=render", article["title"], "readings", "pmc-13346298", expected="pdf")
    if not item.get("markdown_path"):
        raise ValueError("The recovered full-text PDF was not converted")
    item["aliases"] = ["https://pubmed.ncbi.nlm.nih.gov/39954218/", "https://europepmc.org/articles/PMC13346298", "https://pmc.ncbi.nlm.nih.gov/articles/PMC13346298/"]
    item["reading_requirement"] = "project-background"
    item["linked_from"] = [DOC_URL]
    item["notes"].append("The PubMed page returned a cookie wall. Europe PMC resolved PMID39954218 to the same open-access PMCIDPMC13346298 and DOI10.1007/s10803-025-06734-x; a genuine full PDF and JATS body were retrieved.")
    item["full_text_verification"] = {"pmid": "39954218", "pmcid": "PMC13346298", "doi": article["doi"], "metadata_path": "raw/metadata/pubmed-39954218-europepmc.json", "jats_path": "raw/readings/pmc-13346298.xml", "parsed_jats_path": "raw/metadata/pmc-13346298-parsed.json", "section_count": parsed["section_count"], "word_count": parsed["word_count"]}
    failed = next(record for record in corpus.data["materials"] if record["url"] == "https://pubmed.ncbi.nlm.nih.gov/39954218/")
    failed["recovered_by"] = item["markdown_path"]
    failed.setdefault("rejected_markdown_path", "markdown/project-references/pubmed-ncbi-nlm-nih-gov-39954218.md")
    endpoint = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urlencode({"query": "EXT_ID:39954218 AND SRC:MED", "format": "json", "pageSize": 1, "resultType": "core"})
    metadata = add_snapshot(corpus, endpoint, "Europe PMC identifier and open-access metadata: PMID39954218", "metadata", "pubmed-39954218-europepmc", metadata_path.read_bytes(), ".json", "source-code-fence", code_block(metadata_path.read_text(encoding="utf-8"), "json"))
    metadata["notes"] = ["Targeted lookup; expected1result, retrieved1result. The record identifies the full-text recovery for the course's project background article."]
    corpus.save()
    update_core_links(corpus)
    for record in corpus.data["materials"]:
        if not record["id"].startswith(record["category"] + "/"):
            record["id"] = record["category"] + "/" + record["id"]
    corpus.write_indexes()
    print(json.dumps({"title": article["title"], "pages": item["page_count"], "verified_sections": parsed["section_count"], "verified_words": parsed["word_count"]}, indent=2))


if __name__ == "__main__":
    main()
