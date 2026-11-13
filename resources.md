# Курсы по разработке AI-агентов

Дата подбора: **13 ноября 2026 года**.

## Цель и критерии

Подборка нужна для проектирования курса весеннего семестра для талантливых первокурсников, которые уже хорошо умеют программировать.

В подборке **25 курсов и практикумов плюс две книги**. Для первого подробного разбора стоит взять **Stanford CS329Z, Columbia, Mannheim, CMU и Michigan**: вместе они дают основу по архитектуре агентов, домашним заданиям и оценке качества.

Рейтинг составлен **по полезности для будущего курса**, с учётом доступности материалов и подготовки студентов. Это оценка программ и опубликованных заданий, а не результатов прохождения курсов.

Свежесть трактуется строго: **13 ноября 2025 — 13 ноября 2026**. Для университетских курсов указана конкретная редакция 2026 года; часть осенних курсов ещё продолжается, поэтому материалы последних занятий пока опубликованы не везде.

Материалы курсов пока **не скачивались**. Ссылки ведут на страницы курсов, программы, задания, репозитории и подтверждения дат запуска.

## Основной корпус: наиболее полезные курсы с подробными материалами

Первые 13 — наиболее полезный корпус для подробного изучения. **У первых десяти есть существенные материалы сверх программы:** слайды, код, лабораторные или формулировки заданий.

| № | Курс и свежая редакция | Что доступно | Почему стоит изучить |
|---|---|---|---|
| **1** | **[Stanford CS329Z — Engineering AI Agents](https://cs329z.stanford.edu/)**. Осень 2026 | Подробное расписание, слайды, часть видео, чтение; два открытых репозитория домашних работ, правила проекта. | **Лучший общий ориентир для инженерного курса.** Компоненты сначала реализуются самостоятельно, затем изучаются фреймворки. Есть инструменты, память, контекст, мультиагентность, данные и полноценный блок оценивания. |
| **2** | **[Columbia COMS 4995-15 — Designing LLM Agents](https://designing-agents.github.io/)**. Осень 2026 | Слайды, упражнения с решениями, три домашние работы, стартовый код и финальный проект. | **Особенно подходит целевой аудитории:** требуется Python, предварительное знание ML не предполагается. Хорошая последовательность от устройства LLM до памяти, планирования, инструментов и безопасности. |
| **3** | **[Mannheim IE685/IE686 — Large Language Models and Agents](https://www.uni-mannheim.de/dws/teaching/course-details/courses-for-master-candidates/ie-685-large-language-models-and-agents/)**. Весна 2026 | PDF лекций, упражнения с ноутбуками, описание проектов, схема оценивания; даже опубликованы результаты оценки курса студентами. | **Удобный образец организации семестра:** сначала компактный набор основ и практических занятий, затем командный проект с консультациями. Есть отдельные занятия по context engineering и безопасности. |
| **4** | **[CMU 11-768 — AI Agents](https://www.cmu-agents.com/)**. Новый курс, осень 2026 | Программа, слайды и записи; открытые задания и стартовый код по построению harness и оцениванию агента. | **Один из самых содержательных технических ориентиров.** Студенты строят агента, разрабатывают оценки, затем изучают обучение агентов. Блок обучения моделей для первокурсников потребует существенного упрощения. |
| **5** | **[Michigan EECS 498 — Applied Agentic Software Engineering](https://eecs498-aase.github.io/)**. Осень 2026; существенная переработка в октябре | Подробные правила и описания проектов; публичный репозиторий лекций, лабораторных слайдов и демонстраций. Репозитории самих заданий выдаются студентам приватно. | **Сильный подход «использовать → разобрать → расширить».** Студенты изучают настоящие coding agents и добавляют skills, цикл выбора инструментов, shell с разрешениями и MCP. Хороший источник инженерных заданий. |
| **6** | **[Google × Kaggle — 5-Day AI Agents: Intensive Vibe Coding](https://www.kaggle.com/learn-guide/5-day-agents-vibecoding)**. Переработанный запуск, 15–19 июня 2026 | Пять тематических white papers, codelabs, записи эфиров, задания и capstone. | **Богатый практический набор:** инструменты и протоколы, skills, безопасность, оценки, развёртывание. Значительная часть практики посвящена разработке через Antigravity, поэтому материалы для курса придётся отбирать. |
| **7** | **[MIT IAP NANDA — AI Agent Development](https://github.com/projnanda/5-day-course)**. Январский интенсив 2026 | Открытый репозиторий с программой по дням, инструкциями и кодом. | **Хороший образец короткого вводного проекта:** простой агент → память и MCP → API и deployment → взаимодействие агентов → финальное соревнование. Заметно проще для адаптации, чем исследовательский магистерский курс. |
| **8** | **[University of Virginia CS6501 — Workshop on Building AI Agents](https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/agenticAI.html)**. Весна 2026 | Календарь, презентации, практические задания по темам, требования к портфолио и большой список проектов. | **Полезная педагогическая модель:** основное программирование проходит на занятиях; оцениваются GitHub-портфолио и работающая система. Можно заимствовать задания по инструментам, RAG, протоколам и управлению контекстом. |
| **9** | **[LangChain Academy — Introduction to LangChain, Python](https://academy.langchain.com/courses/foundation-introduction-to-langchain-python)**. Запуск в декабре 2025 | 30 уроков, транскрипты, открытые ноутбуки и три проекта: personal chef, wedding planner, email assistant. | **Удобный источник небольших лабораторных:** tools, память, MCP, мультиагентность, middleware и human-in-the-loop. Однако объяснение архитектуры придётся дополнять: курс быстро вводит готовые абстракции LangChain. |
| **10** | **[LangChain Academy — Introduction to Deep Agents](https://academy.langchain.com/courses/foundation-introduction-to-deepagents)**. Запуск в июле 2026 | Подробная программа, бесплатные уроки, открытый репозиторий практики. | **Хороший источник современной инфраструктуры агента:** файловая система, песочницы, управление контекстом, skills, память, делегирование и вмешательство человека. Подходит для второй половины семестра. |
| **11** | **[Leiden — Agentic Large Language Models](https://agenticllms.liacs.nl/)**. Новый курс, осень 2026 | Подробная программа и календарь, описание четырёх программных case studies, открытый учебник преподавателей. | **Хороший академический противовес фреймворкам:** reasoning, действия, инструменты и взаимодействие агентов. Полный курс предполагает ML, PyTorch и RL; для первокурсников полезнее отдельные темы и проекты. |
| **12** | **[Stanford CS224V — Agentic AI](https://web.stanford.edu/class/cs224v/)**. Осень 2026, с новыми заданиями этого семестра | Слайды, подробное расписание, две домашние работы с Colab, материалы проекта. | **Особенно ценен подход к надёжности:** проверяемые основания ответов, исследовательские агенты, структурированные данные, ограничения и анализ ошибок. Тематика местами специализированная — медицина и научный поиск. |
| **13** | **[Johns Hopkins EN.601.727 — Machine Programming](https://machine-programming.github.io/)**. Осень 2026 | Программа, лекционные материалы, чтение; три задания с открытым стартовым кодом. | **Источник для блока coding agents.** Особенно интересны задания «оценить coding LLM» и «построить coding agent». Весь курс существенно шире агентов: включает синтез программ и формальные методы. |

### Прямые ссылки на задания и материалы

1. **Stanford CS329Z**:
   - [Assignment 1: Building an Agent Harness — стартовый репозиторий, формулировка и тесты](https://github.com/cs329z/assignment1-harness).
   - [Assignment 2: Building an Evaluation Task](https://github.com/cs329z/assignment2-evals).
   - Слайды, видео и чтение привязаны к занятиям на [главной странице](https://cs329z.stanford.edu/).
2. **Columbia**:
   - [Syllabus](https://designing-agents.github.io/syllabus.html).
   - [Homework 3: Build Your First Agent](https://designing-agents.github.io/HW3.html) — подробная формулировка и ссылка на стартовый код.
   - Остальные задания, слайды, упражнения и решения доступны из [расписания](https://designing-agents.github.io/).
3. **Mannheim**:
   - [Программа и таблица всех материалов](https://www.uni-mannheim.de/dws/teaching/course-details/courses-for-master-candidates/ie-685-large-language-models-and-agents/).
   - [Introduction to LLMs and LLM Agents, PDF](https://www.uni-mannheim.de/media/Einrichtungen/dws/Files_Teaching/Large_Language_Models_and_Agents/FSS2026/IE685_LA_01_Introduction.pdf) — версия от 11 февраля 2026.
   - [Agent Programming using LangChain and MCP, ZIP с ноутбуком](https://www.uni-mannheim.de/media/Einrichtungen/dws/Files_Teaching/Large_Language_Models_and_Agents/FSS2026/IE685_LA_EX_Agent_Programming_LangChain_MCP.ipynb.zip).
4. **CMU**:
   - [Assignment 1: Build an Agent Harness](https://github.com/cmu-agents/assignment-1).
   - [Assignment 2: Evaluating a Data-Visualization Agent](https://github.com/cmu-agents/assignment-2).
   - В обоих репозиториях формулировки находятся в `ASSIGNMENT.md`.
5. **Michigan**:
   - [Syllabus и текущие требования к проектам](https://eecs498-aase.github.io/syllabus.html).
   - [FAQ, включая ограничения доступа к заданиям](https://eecs498-aase.github.io/faq.html).
   - [Открытые лекционные и лабораторные материалы, демонстрации](https://github.com/eecs498-aase/materials).
   - При расхождениях между страницами и старым README ориентироваться на актуальный syllabus: курс перерабатывался в октябре 2026.
6. **Google × Kaggle**:
   - [Self-paced guide с материалами и codelabs по дням](https://www.kaggle.com/learn-guide/5-day-agents-vibecoding).
   - [Анонс нового запуска: даты и подтверждение обновления программы](https://blog.google/innovation-and-ai/technology/developers-tools/kaggle-genai-intensive-course-vibe-coding-june-2026/).
   - [Итоги запуска и подтверждение доступности материалов для самостоятельного изучения](https://blog.google/innovation-and-ai/technology/developers-tools/ai-agents-intensive-recap-2026/).
7. **MIT IAP NANDA**:
   - [Репозиторий курса с программой, инструкциями по дням и кодом](https://github.com/projnanda/5-day-course).
   - В README курс явно обозначен как подготовленный для MIT IAP 2026.
8. **University of Virginia**:
   - [Программа, оценивание и идеи проектов](https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/agenticAI.html).
   - [Календарь со ссылками на темы, упражнения и презентации](https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/Calendar.html).
9. **LangChain Foundations**:
   - [Программа курса](https://academy.langchain.com/courses/foundation-introduction-to-langchain-python).
   - [Репозиторий ноутбуков и проектов](https://github.com/langchain-ai/lca-lc-foundations).
   - [Обсуждение запуска и публикации репозитория 18–19 декабря 2025](https://forum.langchain.com/t/repository-missing/2550).
10. **LangChain Deep Agents**:
    - [Программа курса](https://academy.langchain.com/courses/foundation-introduction-to-deepagents).
    - [Репозиторий материалов](https://github.com/langchain-ai/lca-deepagents).
    - [Инструкция для Python-версии](https://github.com/langchain-ai/lca-deepagents/blob/main/python/README.md).
    - [Видеоанонс нового курса от LangChain, 7 июля 2026](https://www.youtube.com/watch?v=z30BJFWe89c).
11. **Leiden**:
    - [Syllabus: предпосылки, результаты обучения и оценивание](https://agenticllms.liacs.nl/syllabus/).
    - [Календарь с четырьмя case studies](https://agenticllms.liacs.nl/schedule/).
    - [Ресурсы](https://agenticllms.liacs.nl/resources/).
    - [Описание курса преподавателем](https://www.nikivanstein.nl/teaching/2026-agentic-llms).
12. **Stanford CS224V**:
    - [Расписание и слайды](https://web.stanford.edu/class/cs224v/schedule.html).
    - [Homework 1: Finding the Patient — Agentic Literature Research for Rare-Disease Diagnosis, PDF](https://web.stanford.edu/class/cs224v/cs224v_2026_hw1.pdf).
    - [Homework 2: ReAct Agents, AOS, SatIR and VERDICT, PDF](https://web.stanford.edu/class/cs224v/cs224v_2026_hw2.pdf).
13. **Johns Hopkins Machine Programming**:
    - [Страница всех заданий, правил и доступа к моделям](https://machine-programming.github.io/assignments.html).
    - [Репозиторий Assignment 2: Evaluating Coding LLMs](https://github.com/machine-programming/assignment-2).
    - [Репозиторий Assignment 3: Coding LLM Agents](https://github.com/machine-programming/assignment-3).

## Дополнительные курсы: отдельные темы и организация проектов

Следующие пять полезны для отдельных частей курса или организации проектов. Доступ к полному комплекту практики здесь менее удобен.

| № | Курс и дата | Что доступно и зачем смотреть |
|---|---|---|
| **14** | **[DeepLearning.AI × Chroma — Context Engineering](https://www.deeplearning.ai/courses/context-engineering)**. 20 октября 2026 | Публичное описание и **PDF слайдов четырёх модулей**; обучение и задания — на платформе. Полезен как специализированный источник по выбору и организации информации, которую получает агент. |
| **15** | **[DeepLearning.AI × Arize — Evaluating and Improving Agentic Applications](https://www.deeplearning.ai/courses/evaluating-and-improving-agentic-applications)**. 4 ноября 2026 | Опубликованы **слайды пяти модулей**: основы оценивания, наблюдаемость и бенчмарки, проверка evaluators, оценка действий и результатов, улучшение системы. Особенно полезен для проектирования требований к студенческим экспериментам. |
| **16** | **[MIT AI Studio — From AI Agents to the Agentic Web](https://aiforimpact.github.io/fall26.html)**. Осень 2026 | Публичны программа и требования к проектам; подробные задания находятся в Canvas. **Интересна последовательность одного большого проекта:** индивидуальный агент → команда агентов → агентная организация в общей среде NANDA Town. |
| **17** | **[CU Boulder CSCI7000 — Building AI Agents](https://danny.cs.colorado.edu/courses/csci7000-009_F26/index.html)**. Осень 2026 | Подробный план чтения, требования к проекту, рецензиям и докладам. **Хороший источник семинарских тем** по программным агентам, их отказам и оцениванию; меньше подходит как готовый набор вводных лабораторных. |
| **18** | **[UT Austin INF385T — Building Large Language Model Applications](https://jiaxin-pei.github.io/courses/inf385t/)**. Новый курс, осень 2026 | Подробная программа, чтение и часть домашних заданий; код и упражнения — в Canvas. **Полезен для проектной составляющей:** реальные пользователи, прототипы, проверка продукта и несколько demo days. Значительная часть курса посвящена стартапам. |

### Дополнительные ссылки и подтверждения дат

- **Context Engineering**:
  - [Анонс запуска 20 октября 2026](https://community.deeplearning.ai/t/new-course-enroll-in-context-engineering/895768).
  - [Lecture Notes: четыре PDF-модуля](https://community.deeplearning.ai/t/context-engineering-lecture-notes/895744).
- **Evaluating and Improving Agentic Applications**:
  - [Анонс запуска 4 ноября 2026](https://community.deeplearning.ai/t/new-course-enroll-in-evaluating-and-improving-agentic-applications/896149).
  - [Lecture Notes: пять PDF-модулей](https://community.deeplearning.ai/t/evals-lecture-notes/896118).
- **MIT AI Studio**: [страница осеннего курса 2026 с требованиями к проектам и Demo Day](https://aiforimpact.github.io/fall26.html).
- **CU Boulder**: [программа осеннего семестра 2026](https://danny.cs.colorado.edu/courses/csci7000-009_F26/index.html), включая ссылки на syllabus, research project, paper critiques и paper presentation.
- **UT Austin**:
  - [Официальная университетская карточка курса](https://ischool.utexas.edu/programs/class-schedules/inf-385t-special-topics-information-science-building-large-language-model).
  - [Подробная программа преподавателя](https://jiaxin-pei.github.io/courses/inf385t/).
  - [Университетская новость о новом курсе, 20 октября 2026](https://ischool.utexas.edu/news/new-ai-startup-class-helps-ut-students-turn-ideas-real-products).

## Узкие практикумы для отдельных занятий

Следующие семь — **узкие практикумы для отдельных занятий**, а не образцы полного семестра. У DeepLearning.AI публичны программы; видео и практические материалы предоставляются через платформу, а часть проверяемых заданий относится к Pro.

| № | Практикум и дата запуска | Что из него брать |
|---|---|---|
| **19** | **[Agent Skills with Anthropic](https://www.deeplearning.ai/alpha/short-courses/agent-skills-with-anthropic)**. 28 января 2026 | Десять видеоуроков: устройство skills, отличие от tools/MCP/subagents, создание собственных навыков, использование через API и Agent SDK. **Хорошее занятие про расширяемость агента.** |
| **20** | **[Building Coding Agents with Tool Execution — E2B](https://www.deeplearning.ai/courses/building-coding-agents-with-tool-execution)**. 3 декабря 2025 | Пять примеров кода; агент пишет и выполняет программы, работает с файлами и исправляет ошибки по обратной связи. **Практика по CodeAct и изолированному исполнению кода.** |
| **21** | **[Agent Memory: Building Memory-Aware Agents — Oracle](https://www.deeplearning.ai/courses/agent-memory-building-memory-aware-agents/)**. 18 марта 2026 | Семь видеоуроков и четыре примера кода: memory manager, поиск инструментов, извлечение и консолидация памяти, сохранение между сессиями. **Хорошая основа лабораторной по долговременной памяти**, хотя реализация привязана к Oracle. |
| **22** | **[Loop Engineering with LangChain Deep Agents](https://www.deeplearning.ai/courses/loop-engineering-with-langchain-deep-agents)**. 28 октября 2026 | Циклы выполнения, проверки результата, запуска по событиям и улучшения по предыдущим трассам. **Полезен для перехода от демонстрации агента к системе, которая проверяет и улучшает свою работу.** |
| **23** | **[Building Adaptive AI Agents — Oracle](https://www.deeplearning.ai/courses/building-adaptive-ai-agents)**. 26 августа 2026 | Превращение трасс в повторно используемые skills, работа с code knowledge graphs, выбор между улучшением контекста и дообучением. **Источник для продвинутого проекта про накопление опыта агентом.** |
| **24** | **[A2A: The Agent2Agent Protocol — Google Cloud / IBM](https://www.deeplearning.ai/courses/a2a-the-agent2agent-protocol)**. 12 февраля 2026 | 14 видеоуроков, восемь примеров кода; соединение агентов из разных фреймворков. **Хорошая практическая иллюстрация протоколов взаимодействия**, после освоения обычных инструментов и MCP. |
| **25** | **[Nvidia’s NeMo Agent Toolkit: Making Agents Reliable](https://www.deeplearning.ai/courses/nvidia-nat-making-agents-reliable)**. 17 декабря 2025 | Девять видеоуроков, шесть примеров кода: tracing, оценки, поиск ошибок, мультиагентность и deployment. **Компактный практикум по наблюдаемости и надёжности**, с привязкой к NeMo Agent Toolkit. |

### Источники дат запуска и дополнительные материалы

- **Agent Skills with Anthropic** — [анонс 28 января 2026](https://community.deeplearning.ai/t/new-course-enroll-in-agent-skills-with-anthropic/887920).
- **Building Coding Agents with Tool Execution** — [анонс 3 декабря 2025](https://community.deeplearning.ai/t/new-course-enroll-in-building-coding-agents-with-tool-execution/884418).
- **Agent Memory**:
  - [Анонс 18 марта 2026](https://community.deeplearning.ai/t/new-course-enroll-in-agent-memory-building-memory-aware-agents/890523).
  - [Объявление и описание программы от Oracle](https://blogs.oracle.com/developers/oracle-and-deeplearning-ai-launch-new-agent-memory-course-for-ai-developers).
- **Loop Engineering** — [анонс 28 октября 2026](https://community.deeplearning.ai/t/new-course-enroll-in-loop-engineering-with-langchain-deep-agents/895960).
- **Building Adaptive AI Agents**:
  - [Анонс 26 августа 2026](https://community.deeplearning.ai/t/new-course-enroll-in-building-adaptive-ai-agents/894827).
  - [Описание содержания от Oracle](https://blogs.oracle.com/developers/we-just-launched-a-new-course-on-how-to-build-adaptive-ai-agents).
- **A2A** — [анонс 12 февраля 2026](https://community.deeplearning.ai/t/new-course-enroll-in-a2a-the-agent2agent-protocol/888762).
- **NeMo Agent Toolkit** — [анонс 17 декабря 2025](https://community.deeplearning.ai/t/new-course-enroll-in-nvidias-nemo-agent-toolkit-making-agents-reliable/885253).

## Книги

| Книга | Доступ и польза |
|---|---|
| **[An Illustrated Guide to AI Agents — Maarten Grootendorst, Jay Alammar](https://www.oreilly.com/library/view/an-illustrated-guide/9798341662681/)**. Сентябрь 2026 | Платная, **подробное оглавление открыто**. Покрывает память, инструменты и протоколы, планирование, reflection, оценки, мультиагентность и coding agents. По структуре выглядит особенно подходящим кандидатом на сопровождающий учебник. |
| **[Agentic Large Language Models — van Duijn, van der Meer, Plaat, van Stein](https://arxiv.org/abs/2610.13455)**. Октябрь 2026 | **Полный текст свободно доступен**, 472 страницы; связан с курсом Leiden. Более академический источник для преподавателя и сильных студентов, включая reasoning, обучение и поведение мультиагентных систем. |

Дополнительный источник по второй книге: [анонс автора от 16 октября 2026](https://www.nikivanstein.nl/posts/2026/10/agentic-llms-book/), подтверждающий доступность полного текста на arXiv и связь с новым курсом Leiden.

## Приоритет для следующего этапа

- **Stanford CS329Z** — основной каркас инженерного курса.
- **Columbia и Mannheim** — последовательность практики и организация семестра.
- **CMU** — задания на harness и оценки.
- **Michigan** — разбор настоящих coding agents и расширение существующих реализаций.
- **Короткие практикумы** — отдельные лабораторные по памяти, skills и исполнению кода.

### Особенно интересная педагогическая находка

В [домашней работе Stanford CS224V на анализ ошибок](https://web.stanford.edu/class/cs224v/cs224v_2026_hw1.pdf) вызовы моделей уже выполнены. Студенты исследуют сохранённые промежуточные результаты, а баллы получают за объяснение причин успеха или провала. Это позволяет проверять понимание агента независимо от качества сгенерированного студентом кода.

В формулировке отдельно подчёркнуто: правильный диагноз без объяснения получает меньше баллов, чем неудачный результат с точным объяснением места отказа. Количественные утверждения должны опираться на конкретные результаты в ноутбуке; студент должен найти хотя бы одну ошибку через целенаправленное исследование pipeline.
