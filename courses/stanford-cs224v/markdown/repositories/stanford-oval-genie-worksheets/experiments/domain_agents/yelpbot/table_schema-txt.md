# Project code: stanford-oval/genie-worksheets: experiments/domain_agents/yelpbot/table_schema.txt

[Course index](../../../../../../README.md) · [Original source](https://github.com/stanford-oval/genie-worksheets/blob/HEAD/experiments/domain_agents/yelpbot/table_schema.txt) · [Raw file](../../../../../../raw/repositories/stanford-oval-genie-worksheets/experiments/domain_agents/yelpbot/table_schema.txt)

Retrieved: 2026-11-13T17:06:24.900930+00:00

```txt
CREATE TABLE restaurants (
    _id INT PRIMARY KEY,
    name TEXT,
    cuisines TEXT[],
    price ENUM ('cheap', 'moderate', 'expensive', 'luxury'),
    rating NUMERIC(2,1),
    num_reviews NUMBER,
    popular_dishes FREE_TEXT,
    phone_number TEXT,
    reviews FREE_TEXT,
    opening_hours TEXT,
    location TEXT
);

yelp_general_info : FREE_TEXT;
```
