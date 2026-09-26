# Interview questions and answers / Вопросы и ответы для собеседований

## 1. Вопрос

How many years of hands-on experience do you have in ML and NLP, and which ML or LLM features have you shipped to production?

**Ответ:**

I have about four and a half years of experience in a dedicated ML role, from 2014 to 2018, when I applied classical models to actuarial and insurance data. After that, I focused on backend engineering and system architecture. Since 2025, I've been building production LLM applications, drawing on that engineering background.

My main project is Aiva, a voice and chat AI platform that I developed from scratch. I designed the backend and agent architecture, integrated telephony and model providers, and handled deployment and monitoring. The agents support inbound enquiries, lead qualification, customer support, and outbound campaigns. They can retrieve information from a knowledge base, call business tools, transfer a conversation to a person, and save the outcome in a CRM.

Much of my recent work has involved making these interactions reliable: handling interruptions and disconnected sessions, diagnosing latency, and ensuring that a call result is saved before the session closes.

## 2. Вопрос

Have you fine-tuned open-source LLMs such as Llama, Mistral, or Qwen using LoRA, PEFT, or similar methods? If so, what was the task and the outcome?

**Ответ:**

I haven't fine-tuned open-source LLMs with LoRA, PEFT, or similar methods. My recent work has focused on integrating models into production applications through APIs, prompts, tool calling, and RAG.

For example, in Aiva I built the path from a business knowledge base to an agent's answer: document processing, embeddings, vector retrieval, and passing relevant context to the model. I also integrated several providers for real-time voice conversations and implemented the surrounding application logic, including call handling, CRM integration, and monitoring.

I have worked with vLLM as inference infrastructure. My hands-on experience with LLMs is strongest in application engineering and operating agents in production; I don't have a fine-tuning project or training results to present.

## 3. Вопрос

Do you have commercial experience with LLMs? Which frameworks and tools have you used?

**Ответ:**

Yes. I developed Aiva, a production platform for voice and chat AI agents, and was responsible for its technical architecture, backend, integrations, deployment, and monitoring. The platform supports business scenarios such as lead qualification, customer support, and outbound calls.

For voice, I integrated Google Gemini, OpenAI Realtime, and xAI/Grok Voice through provider adapters. The agents work with SIP telephony and use tools to search a knowledge base, record an outcome, transfer a call, or end the conversation. For chat, I used Gemini with LangChain, Redis for conversation history, and Langfuse for tracing model requests.

The RAG pipeline uses Yandex AI Studio embeddings and PostgreSQL with pgvector, with source documents stored in S3. The backend is built with Python and FastAPI. I also have separate experience with vLLM for model inference.

## 4. Вопрос

How have you evaluated the quality of ML or LLM features? Have you used evaluation datasets, LLM-as-a-judge, or A/B testing?

**Ответ:**

I've built an LLM-as-a-judge evaluation pipeline and have hands-on experience with automated evaluation of LLM outputs. My broader evaluation work also includes end-to-end testing of agents and monitoring their behavior in production.

At Sber, I joined a new two-person team as a developer and MLOps engineer to build an anomaly-monitoring service for AI agents developed by different product teams. I defined the service boundaries and logic, selected a scientific approach to detecting deviations, and implemented it. We took the service into production in four months. This gave me additional experience building infrastructure for monitoring agent behavior.

In Aiva, I test the complete voice-agent journey: connection, model and voice selection, tool calls, handoff, and call completion with the result saved. I use real SIP calls and smoke tests, correlate logs across the API, voice worker, media server, and SIP layer, and inspect chat traces in Langfuse. The operational metrics include time to first token, response duration, token usage, speech recognition and synthesis metrics, and call outcomes.

I don't have measured A/B test results or a dedicated benchmark dataset for Aiva to share.

## 5. Вопрос

Do you have commercial experience with Python? Which frameworks and libraries have you used?

**Ответ:**

Yes. Python has been my main language in commercial development for more than 10 years. My work has ranged from ML and bioinformatics data pipelines to backend services, API integrations, and production AI applications.

In Aiva, I use FastAPI and asyncio for the backend and asynchronous workflows, SQLAlchemy with PostgreSQL for persistent data, and Redis for temporary state and chat history. I also write background jobs, integration code, and tests. One example is the knowledge-base pipeline, which reads source documents, splits them into overlapping chunks, requests embeddings, and stores them for vector retrieval.

I've also dealt with concurrency and task lifecycle problems. For example, I fixed a race during call termination where an asynchronous task could be cancelled before it saved the call result. My Python experience includes both implementing features and investigating their behavior across services in production.

## 6. Вопрос

Do you have commercial experience with LLMs? Which frameworks and tools have you used?

**Ответ:**

Yes. My main recent experience is building Aiva, a voice and chat AI platform for business use. I developed the backend and agent execution logic, connected model providers and telephony, and took the system through deployment and production support.

I used Gemini with LangChain for chat, Redis for conversation history, and Langfuse for tracing. For voice agents, I integrated Gemini, OpenAI Realtime, and xAI through separate adapters. That work included real-time audio sessions, tool calling, interruption handling, and SIP telephony.

I also built the knowledge retrieval pipeline using Yandex AI Studio embeddings and PostgreSQL with pgvector. Agents use it to answer from business documents, then save call outcomes or pass information to a CRM. Alongside this application work, I have experience with vLLM as model inference infrastructure.

## 7. Вопрос

Which part of your background makes you a strong fit for this role?

**Ответ:**

My strongest fit is the ability to take an AI product from a business requirement through to production and remain responsible for how it works after launch. I have more than 10 years of backend experience, including architecture work, and I've applied that background to building Aiva from scratch.

In Aiva, I designed the backend and agent architecture, integrated telephony, model providers, knowledge retrieval, and CRMs, and handled deployment and monitoring. I also investigated practical problems such as delayed responses, interrupted conversations, and call results being lost during session shutdown.

Earlier, at Samokat, I designed the architecture for a Backend-Driven UI project, defined service boundaries and API contracts, documented decisions in ADRs, and reviewed them with platform architects. That combination gives me experience with both architecture in a larger organization and hands-on ownership of a product across its full technical lifecycle.

## 8. Вопрос

Give one brief, concrete example that demonstrates your ambition, initiative, and commitment.

**Ответ:**

Since 2025, I've built Aiva, my voice AI platform, from scratch and taken it into production. I learned the telephony protocols, selected reusable open-source components, designed the backend and agents, and integrated models, knowledge retrieval, and CRMs. I also took responsibility for deployment, monitoring, and diagnosing problems in real calls. The result is a multi-user platform for voice and chat agents, with teams, roles, and access controls.

Earlier, I co-founded a grocery delivery startup and led software development through the launch of our first dark store in Minsk in October 2020. We delivered customer and courier apps, warehouse tools, and the order-to-delivery workflow alongside the physical operation.

## 9. Вопрос

Расскажите кратко о вашем опыте технического лидерства, наставничества и проектирования архитектуры.

**Ответ:**

В Aiva я разработал с нуля платформу голосовых и чат-агентов для бизнеса и сейчас развиваю ее вместе с небольшой командой. Я отвечаю за продукт и техническую реализацию: изучил телефонные протоколы, выбрал открытые компоненты для переиспользования, спроектировал архитектуру и построил техническое ядро платформы.

В мою зону ответственности входят backend на Python и FastAPI, работа агентов, интеграции с моделями и телефонией, база знаний, CRM, развертывание и мониторинг. Я реализовал входящие и исходящие звонки, поиск по базе знаний, перевод на сотрудника и сохранение результатов. Платформа поддерживает отдельных пользователей и команды, роли и права доступа. После запуска я также занимался диагностикой задержек, разрывов сессий и ошибок при завершении звонков.

В Самокате я пришел в проект Backend-Driven UI почти в самом начале и отвечал за архитектуру. Определял API-контракты и границы сервисов, готовил диаграммы и ADR, защищал решения перед архитекторами платформы. Мой опыт технического лидерства связан с ответственностью за эти решения и их реализацию. Формальной роли наставника у меня не было.

## 10. Вопрос

Был ли у вас опыт наставничества или руководства командой?

**Ответ:**

У меня есть опыт технического лидерства в небольшой продуктовой команде. Сейчас в Aiva я отвечаю за продукт и разработку: определяю архитектуру платформы, выбираю технические решения и участвую в реализации, интеграциях и эксплуатации. Это требует учитывать, как изменения в агентах, backend, телефонии и инфраструктуре влияют на работу всей системы.

Ранее в Самокате я отвечал за архитектуру Backend-Driven UI, оформлял решения в документации и ADR и обсуждал их с архитекторами платформы. Моя ответственность заключалась в том, чтобы определить устройство системы и обосновать принятые решения.

В роли линейного руководителя я не работал. Отдельного примера, где можно показать рост сотрудника под моим формальным наставничеством с исходным уровнем, результатом и сроками, у меня пока нет.

## 11. Вопрос

Приходилось ли вам одновременно вести несколько проектов или инициатив? Сколько направлений вы координировали?

**Ответ:**

В Aiva я параллельно вел несколько связанных направлений внутри одного продукта: backend, среду выполнения агентов, телефонию, базу знаний и RAG, CRM-интеграции, развертывание и мониторинг. Для каждого из них требовались свои технические решения, при этом пользовательский сценарий проходил сразу через несколько частей системы.

Например, исходящая кампания объединяет загрузку контактов, расписание с учетом часовых поясов, запуск звонка, работу агента, сохранение результата и аналитику. Я занимался как отдельными компонентами, так и их взаимодействием. Поэтому мой опыт включает координацию нескольких направлений разработки с общими зависимостями и единым результатом.

Формальным портфелем независимых проектов я не управлял. Точное максимальное число одновременно ведущихся проектов назвать не могу: перечисленные направления были частями одной платформы.

## 12. Вопрос

Запускали ли вы AI-проекты от идеи до пилота или внедрения?

**Ответ:**

Да, у меня есть два примера. В Сбере я присоединился к новой команде из двух человек как разработчик и MLOps-инженер. Мы создавали сервис мониторинга аномалий для AI-агентов, которых разрабатывали разные продуктовые команды. Я продумал границы и логику сервиса, подобрал научный подход к обнаружению отклонений и реализовал его. За четыре месяца мы запустили сервис в production. После запуска фокус работы сместился к настройке модели LSTM. Мне было интереснее продолжать строить и развивать саму систему.

Второй пример связан с собственной платформой Aiva, которую я разработал с нуля. Здесь моя ответственность охватывала весь цикл: выбор бизнес-сценариев, изучение телефонии и доступных компонентов, проектирование архитектуры, реализацию backend и агентов, интеграции и запуск.

В результате появились голосовые и чат-агенты для приема обращений, поддержки, квалификации лидов и исходящих кампаний. Я также построил RAG, подключил CRM и организовал мониторинг. После запуска продолжил работать с поведением системы в реальных звонках: задержками, перебиваниями, разрывами соединений и сохранением результатов.

## 13. Вопрос

Расскажите об успешном примере внедрения AI в бизнес-процессы. Какую задачу вы решали и за что отвечали?

**Ответ:**

В Aiva я реализовал автоматизацию клиентских коммуникаций через голосовых и чат-агентов. Один из основных сценариев связан с обработкой обращения: агент принимает звонок, отвечает на вопросы по базе знаний компании, квалифицирует обращение, при необходимости переводит разговор на сотрудника и сохраняет результат в CRM.

Есть и исходящие кампании. Пользователь загружает контакты и задает расписание с учетом часовых поясов, после чего платформа запускает звонки и собирает их результаты. Для этого я связал телефонию, модели для диалога в реальном времени, backend, RAG и бизнес-интеграции, включая Bitrix24 и amoCRM.

Моя зона ответственности включала архитектуру и реализацию этого процесса, а также развертывание и диагностику. Например, пришлось отдельно решать проблему сохранения результата при завершении голосовой сессии. В результате получился работающий процесс от обращения или запуска кампании до фиксации итога в CRM. Данных, позволяющих точно оценить экономию или рост конверсии, у меня нет.

## 14. Вопрос

Расскажите кратко о вашем опыте технического лидерства, наставничества и проектирования архитектуры.

**Ответ:**

В Aiva я разработал с нуля платформу голосовых и чат-агентов для бизнеса и сейчас развиваю ее вместе с небольшой командой. Я отвечаю за продукт и техническую реализацию: изучил телефонные протоколы, выбрал открытые компоненты для переиспользования, спроектировал архитектуру и построил техническое ядро платформы.

В мою зону ответственности входят backend на Python и FastAPI, работа агентов, интеграции с моделями и телефонией, база знаний, CRM, развертывание и мониторинг. Я реализовал входящие и исходящие звонки, поиск по базе знаний, перевод на сотрудника и сохранение результатов. Платформа поддерживает отдельных пользователей и команды, роли и права доступа. После запуска я также занимался диагностикой задержек, разрывов сессий и ошибок при завершении звонков.

В Самокате я пришел в проект Backend-Driven UI почти в самом начале и отвечал за архитектуру. Определял API-контракты и границы сервисов, готовил диаграммы и ADR, защищал решения перед архитекторами платформы. Мой опыт технического лидерства связан с ответственностью за эти решения и их реализацию. Формальной роли наставника у меня не было.

## 15. Вопрос

At Prosper, we value a consistent record of achievement. In chronological order, list the academic, professional, or personal accomplishments that best demonstrate your ambition and discipline.

**Ответ:**

- **2014:** Graduated in Computer Systems Engineering and began working with machine learning on actuarial and insurance data. This was the start of my professional work with data and software systems.
- **2018–2020:** Studied bioinformatics at Shanghai Jiao Tong University, built research data pipelines, and contributed to scientific publications.
- **2020:** Co-founded a grocery delivery business and led software development through the launch of its first dark store in Minsk in October. The launch included customer and courier apps, warehouse tools, and the order-to-delivery workflow.
- **2020–2025:** Built backend systems at X5 and Rive, then took responsibility for the Backend-Driven UI architecture at Samokat. I defined API contracts and service boundaries, wrote architectural documentation and ADRs, and defended decisions in reviews with platform architects.
- **Since 2025:** Built Aiva, my voice and chat AI platform, from scratch. My work covers backend and agent architecture, telephony, model integrations, knowledge retrieval, CRMs, deployment, and monitoring. The platform supports multiple users and teams with roles and access controls.

Across these projects, I've repeatedly taken responsibility for building systems and bringing them into operation, including both software and the practical work needed to support a launch.

## 16. Вопрос

Можете привести конкретный пример развития сотрудника под вашим наставничеством? С какого уровня он начинал, чего достиг и за какой срок?

**Ответ:**

У меня пока нет примера, где я мог бы описать рост конкретного сотрудника под моим наставничеством, назвать его исходный уровень, результат и сроки. Формальной роли наставника у меня не было.

Ближайший по содержанию опыт связан с техническим лидерством. В Самокате я проектировал архитектуру, готовил документацию и ADR, объяснял и защищал решения перед архитекторами платформы. В Aiva отвечаю за продукт и техническую реализацию в небольшой команде. Эти примеры позволяют предметно обсудить мою ответственность за техническое направление, но оценивать по ним результаты индивидуального наставничества было бы преждевременно.

## 17. Вопрос

Расскажите о важном архитектурном решении с высокой ценой ошибки. Какие варианты вы рассматривали, что выбрали и какие риски приняли?

**Ответ:**

В Aiva нужно было выбрать способ учета минут при параллельных звонках. Один из вариантов заключался в резервировании всего возможного расхода до начала разговора. Он потребовал бы дополнительных блокировок и усложнил запуск звонка. Я выбрал списание после завершения, по фактической длительности.

В этой схеме я предусмотрел две защиты. Списание выполняется в транзакции с блокировкой платежного профиля, чтобы параллельные операции корректно обновляли баланс. Идентификатор звонка используется для защиты от повторного списания за один и тот же разговор.

У решения есть бизнес-компромисс: если пакет минут исчерпан во время звонка, часть секунд может остаться неоплаченной, при этом долг клиенту не начисляется. Этот риск был принят осознанно. Выбранная схема упрощает обработку живого разговора, а учет фактической длительности и защита от повторного списания остаются в транзакционной части backend. Это пример решения, где мне пришлось одновременно учитывать поведение системы при конкурентных запросах и правила расчетов с клиентом.

## 18. Вопрос

Расскажите о серьезном инциденте в production, за устранение которого вы отвечали. Как нашли причину, исправили проблему и предотвратили ее повторение?

**Ответ:**

В Aiva был сбой при завершении исходящих звонков: голосовая сессия могла закрыться, пока асинхронная задача еще отправляла результат разговора в API. Задача отменялась, и статус звонка или данные кампании могли не сохраниться. С точки зрения телефонии разговор уже завершился, но его бизнес-результат терялся.

Мы воспроизвели отмену задачи и сопоставили последовательность событий по логам. Причина оказалась в порядке завершения сессии и жизненном цикле асинхронной операции. Я вынес отправку результата в отдельную задачу и защитил ее с помощью `asyncio.shield`. Также изменил порядок действий: завершение исходящего звонка стало зависеть от успешного сохранения результата.

Дополнительно я добавил проверку повторного вызова и тесты на последовательность сохранения и завершения. Исправление затронуло и управление задачами, и прикладные правила окончания разговора. Для диагностики подобных проблем я использовал логи одного звонка из нескольких сервисов: API, голосового агента, медиасервера и SIP.

## 19. Вопрос

С какой наиболее нагруженной системой вы работали? За какую часть архитектуры отвечали и какие ограничения масштабирования приходилось решать?

**Ответ:**

Я работал с backend мгновенной доставки в X5 и проектировал Backend-Driven UI для мобильного приложения Самоката. В X5 занимался API и внутренними процессами операторов и диспетчеров. В Самокате пришел в проект на ранней стадии и отвечал за архитектуру платформы, которая позволяла менять содержимое и поведение нативного мобильного интерфейса без нового релиза приложения в сторах.

В мою зону ответственности входили API-контракты, конфигурационная модель и границы backend-сервисов. Я готовил архитектурные схемы, фиксировал решения в ADR и защищал их перед архитекторами платформы. Это тот опыт, который я могу подробно разобрать на уровне устройства системы и своей роли.

Точных показателей нагрузки и замеров конкретного узкого места до и после оптимизации у меня нет. Из собственного опыта эксплуатации могу отдельно разобрать Aiva: параллельные звонки, конкурентное списание минут и гонки при завершении голосовых сессий. Для этих задач у меня есть конкретные технические решения, хотя сравнивать масштаб платформы с X5 или Самокатом без цифр я не буду.

## 20. Вопрос

Разрабатывали ли вы AI-агента или мультиагентную систему для реальной бизнес-задачи? Какие инструменты использовали и для чего предназначался продукт?

**Ответ:**

Да. Я с нуля разработал Aiva, платформу голосовых и чат-агентов для бизнеса. Основные сценарии включают прием обращений, поддержку, квалификацию лидов и исходящие кампании. Я отвечал за архитектуру, backend на Python и FastAPI, интеграции, развертывание и мониторинг.

Голосовой агент принимает SIP-звонок через медиасервер и взаимодействует с моделью в реальном времени. Для Gemini, OpenAI Realtime и xAI я реализовал отдельные адаптеры. Через инструменты агент ищет информацию в базе знаний, сохраняет итог разговора, переводит звонок на сотрудника или завершает его. Исходящие кампании включают загрузку контактов, расписание и сбор результатов.

Для чата использовал Gemini с LangChain, Redis для истории и RAG для добавления контекста из документов. Голосовые и чат-сценарии связаны с CRM и другими бизнес-интеграциями. В платформе можно настроить нескольких агентов для разных задач, но они работают независимо, без делегирования между собой.

## 21. Вопрос

Какой у вас опыт работы с Python и JavaScript, в том числе со скриптами и пайплайнами обработки данных?

**Ответ:**

Python я использую в коммерческой разработке больше 10 лет. Начинал с задач ML и обработки данных, работал с исследовательскими пайплайнами в биоинформатике, затем сосредоточился на backend и архитектуре. Пишу асинхронные сервисы, фоновые задания, API-интеграции и тесты; использую FastAPI, asyncio, SQLAlchemy, PostgreSQL и Redis.

В Aiva на Python построены backend, взаимодействие с моделями, голосовые сценарии и обработка базы знаний. Например, фоновый процесс читает документы из S3, разбивает текст на фрагменты, получает эмбеддинги и сохраняет их для поиска через pgvector. Есть также интеграции с телефонией и CRM, где нужно обрабатывать вебхуки, авторизацию и повторные запросы.

JavaScript и TypeScript использую для интерфейсов и интеграционных задач. В моих проектах есть Nuxt/Vue, React/Vite и инструменты Node.js. Основная глубина моего опыта приходится на Python и backend, при этом я работаю и с интерфейсной частью продукта.

## 22. Вопрос

Работали ли вы с платформами для AI-автоматизации, такими как Flowise, n8n, Langflow или Make? Какие интеграции реализовывали?

**Ответ:**

Мой основной опыт AI-автоматизации связан с разработкой интеграций на Python. В Aiva я подключал агентов к Bitrix24, amoCRM, Telegram, WhatsApp, веб-виджетам, телефонии и клиентским API. В сервисах реализовывал авторизацию, обработку вебхуков, передачу данных и повторные попытки запросов.

Конкретный сценарий выглядит так: агент принимает обращение или выполняет исходящий звонок, получает нужную информацию из базы знаний, фиксирует результат и передает его в CRM. При необходимости он переводит разговор на сотрудника. Я разрабатывал как взаимодействие с внешними системами, так и логику агента, который вызывает эти действия.

Проект на Flowise, n8n, Langflow или Make я в качестве примера привести не могу. Мой практический опыт здесь связан с тем, как собрать и эксплуатировать такой процесс в собственных backend-сервисах.

## 23. Вопрос

Какой у вас опыт работы с MCP (Model Context Protocol) и A2A (Agent-to-Agent)?

**Ответ:**

Я знаком с назначением MCP и A2A. MCP используется для подключения инструментов и ресурсов к агенту, A2A предназначен для взаимодействия отдельных агентов. В Aiva я не внедрял эти протоколы в production.

Мой практический опыт относится к самим интеграциям и вызовам инструментов: голосовой агент обращается к поиску по базе знаний, сохраняет результат разговора и переводит звонок на сотрудника. Взаимодействие с моделями реализовано через адаптеры провайдеров, а бизнес-логика находится в сервисах платформы.

Поэтому я могу подробно рассказать об устройстве инструментов, интеграциях и управлении голосовой сессией. Отдельного внедрения MCP или взаимодействия агентов по A2A среди этих проектов нет.

## 24. Вопрос

Как вы проектируете архитектуру AI-агента: вызовы инструментов, память и выполнение многошаговых сценариев? Работали ли вы с ReAct или специализированной средой управления агентами (harness)?

**Ответ:**

В Aiva я проектировал агента как сочетание инструкций, состояния диалога, модели, доступных инструментов и правил завершения сценария. Backend хранит конфигурацию, а голосовая сессия использует выбранный адаптер модели и инструменты для конкретной задачи. Для работы с голосом я интегрировал Gemini, OpenAI Realtime и xAI.

Инструменты позволяют агенту искать информацию в базе знаний, сохранять итог разговора, переводить звонок на сотрудника и завершать его. В чате я использовал Gemini через LangChain, историю диалога в Redis и добавление найденного RAG-контекста перед ответом. Таким образом, состояние разговора, доступ к знаниям и выполнение действий реализованы отдельными частями системы.

На уровне надежности я предусмотрел проверку входных данных, тайм-ауты, повторные попытки внешних вызовов и трассировку. Отдельно разбирал порядок завершения голосовой сессии: результат должен сохраниться до закрытия звонка. Отдельной реализации ReAct или специализированного harness в этом проекте у меня нет; могу предметно описать собственную логику управления сценариями и ее взаимодействие с готовым движком аудиосессий.

## 25. Вопрос

Расскажите о вашем опыте разработки RAG-пайплайнов: разбиении документов, эмбеддингах и векторном поиске. Какие проблемы возникали на реальных данных и как вы их учитывали?

**Ответ:**

Да, в Aiva я разработал полный процесс работы с базой знаний. Документы в форматах `.txt`, `.md` и `.json` хранятся в S3. Фоновый процесс разбивает текст на фрагменты с перекрытием, получает эмбеддинги через Yandex AI Studio и сохраняет их в PostgreSQL с pgvector.

При поиске используется косинусное сходство и фильтры доступа по команде и агенту. В чате найденный контекст добавляется перед генерацией ответа. Голосовой агент обращается к поиску через инструмент во время разговора. Поэтому одна база знаний используется в двух разных сценариях взаимодействия с моделью.

Качество зависит от исходного текста, разбиения документов, актуальности индекса и совместимости моделей эмбеддингов. Я предусмотрел версии индекса, фиксированную модель эмбеддингов, порог релевантности, ограничение объема контекста и повторные попытки индексации. Эти механизмы помогают управлять обновлением базы и тем, какой контекст получает агент. Мой практический опыт в этом проекте связан с pgvector; Qdrant и Chroma я здесь не использовал.

## 26. Вопрос

С какими LLM API и средствами локального развертывания моделей вы работали? Как выбирали провайдера с учетом стоимости, качества и задержек?

**Ответ:**

В Aiva я интегрировал Gemini, OpenAI Realtime и xAI/Grok Voice через отдельные адаптеры. Для чата использовал Gemini с LangChain, для эмбеддингов базы знаний использовал Yandex AI Studio. Также работал с vLLM как с инфраструктурой для запуска моделей, хотя основные агенты платформы обращаются к внешним API.

При выборе голосового провайдера я учитывал задержку ответа, поддержку потокового аудио и инструментов, обработку перебиваний, стоимость и устойчивость API. В реальном звонке все это влияет на диалог: нужно обработать речь пользователя, получить ответ, выполнить действие и корректно продолжить или закончить разговор.

Я занимался и эксплуатационной стороной интеграций: повторными попытками, резервным вариантом обработки при сбоях, трассировкой и диагностикой звонков. Для анализа использовал задержки, расход токенов и логи разных компонентов. Точных сравнительных результатов по стоимости и качеству моделей у меня нет, поэтому могу рассказать о критериях выбора и реализации, но не привести количественный рейтинг провайдеров.

## 27. Вопрос

**Role: Staff DevOps Engineer**

Describe an infrastructure improvement you identified and took from idea to production. What changed as a result, and how did you measure the impact?

**Ответ:**

I built monitoring and diagnostics for Aiva, a production voice AI platform where each call passes through the API, SIP layer, media server, voice worker, and an external model. Investigating a failed call required understanding what happened across those components, so I took responsibility for setting up the monitoring infrastructure and call-level diagnostics.

I provisioned the stack with Terraform and cloud-init, connected Prometheus, Grafana, Loki, and Promtail, and added health checks and dashboards. I also wrote a script to collect logs for one call across services. This gave us a central view of service health and a way to reconstruct the sequence of events for a specific conversation.

I used that approach when investigating problems such as interrupted sessions and call completion failures. For example, correlating events helped diagnose a race where the voice session could close before the result was saved through the API. I don't have a reliable before-and-after measurement of incident resolution time; the concrete result was shared monitoring and a repeatable way to trace a call across the system.

## 28. Вопрос

За какую часть проекта с AI-агентами вы отвечали? Расскажите, что вы разработали и как была устроена система.

**Ответ:**

Я разработал с нуля техническое ядро Aiva и сейчас развиваю платформу вместе с небольшой командой. Моя зона ответственности включает продукт, архитектуру, backend на Python и FastAPI, конфигурацию агентов, интеграции, RAG, развертывание и мониторинг. Платформа поддерживает нескольких пользователей и команды с отдельными ролями и правами доступа.

В голосовом сценарии звонок проходит через SIP-телефонию и медиасервер к агенту, который взаимодействует с моделью через адаптер провайдера. Я реализовал входящие и исходящие звонки, адаптеры Gemini, OpenAI и xAI, поиск по базе знаний, сохранение результата, перевод на сотрудника и запись расшифровки разговора. Для исходящих кампаний есть загрузка контактов, расписание и аналитика.

В чате использовал Gemini через LangChain, Redis для истории и RAG для контекста. База знаний хранит документы в S3 и использует Yandex AI Studio с pgvector для индексации и поиска. После запуска я также отвечал за диагностику звонков и исправление проблем на стыке телефонии, модели и backend.

## 29. Вопрос

Есть ли у вас опыт разработки мультиагентных систем? Как было организовано взаимодействие между агентами?

**Ответ:**

В Aiva можно настроить несколько голосовых и чат-агентов для разных задач и каналов. Каждый работает со своей конфигурацией и доступными ему инструментами. Между ними нет делегирования или общего плана решения задачи, поэтому я не отношу эту платформу к мультиагентным системам.

При этом в собственной разработке я использую несколько AI-агентов для подготовки требований, планирования и ревью. Процесс начинается с описания задачи и контекста, затем агенты помогают сформировать спецификацию, план, список подзадач и вопросы для уточнения. Я проверяю эти материалы и принимаю решения о дальнейшей работе. Для разбора архитектуры использую текст вместе с диаграммами, в том числе ER-диаграммами.

Это опыт применения нескольких агентов в моем инженерном процессе. Отдельного клиентского внедрения, где агенты автономно делегируют работу друг другу и совместно выполняют бизнес-задачу, в описанных проектах нет.

## 30. Вопрос

Как была устроена оркестрация агентов? Использовали ли вы LangGraph, PydanticAI или собственные компоненты?

**Ответ:**

В голосовой части Aiva я использовал готовый движок аудиосессий, а прикладную оркестрацию написал сам. Она включает обработку входящего или исходящего звонка, загрузку конфигурации и промпта, выбор адаптера модели, вызовы инструментов, перевод на оператора и завершение разговора. Для Gemini, OpenAI Realtime и xAI предусмотрены отдельные адаптеры.

Важная часть этой логики связана с жизненным циклом звонка. Например, сохранение бизнес-результата должно завершиться до закрытия исходящей сессии. Я отдельно исправлял гонку между этими операциями, защищал асинхронную задачу от отмены и проверял последовательность тестами.

Для чата использовал LangChain с Gemini и Redis для истории. Загрузку промптов, добавление RAG-контекста, повторные попытки запросов и трассировку реализовал в сервисном слое. LangGraph и PydanticAI в этом проекте не применялись. Основная работа по оркестрации заключалась в управлении состоянием разговора, инструментами и завершением бизнес-сценария.

## 31. Вопрос

Как вы оценивали качество агентной системы и контролировали ее работу в production? Какие метрики и инструменты использовали?

**Ответ:**

У меня есть опыт построения пайплайна оценки через LLM-as-a-judge. Также я занимался сквозным тестированием агентов и мониторингом их поведения в production.

Отдельный проект был в Сбере: я присоединился к новой команде из двух человек как разработчик и MLOps-инженер, чтобы создать сервис мониторинга аномалий для AI-агентов разных продуктовых команд. Я продумал границы и логику сервиса, подобрал научный подход к обнаружению отклонений и реализовал его. За четыре месяца мы запустили сервис в production.

В Aiva я проверял голосовых агентов реальными SIP-звонками и smoke-тестами: соединение, слышимость ответа, выбор модели и голоса, вызовы инструментов, перевод на сотрудника и завершение разговора с сохранением результата. При разборе проблем сопоставлял логи API, голосового агента, медиасервера и SIP. Для этого написал скрипт сбора логов одного звонка из нескольких сервисов.

Система собирает время до первого токена, длительность ответа, расход токенов и метрики распознавания и синтеза речи. Продуктовая аналитика показывает количество, исходы и длительность звонков. Для эксплуатации использовал Prometheus, Grafana, Loki и Sentry, а чат-запросы к LLM отслеживал через Langfuse. Измеренных результатов A/B-тестов для Aiva у меня нет.

## 32. Вопрос

Расскажите о самой сложной системе или задаче, где вы несли значительную техническую ответственность. Какие решения вы принимали самостоятельно?

**Ответ:**

Самой сложной для меня была разработка Aiva с нуля, особенно голосовой части платформы. Нужно было связать SIP-телефонию, медиасервер, модель для диалога в реальном времени, инструменты агента и сохранение результата в CRM. Я отвечал за архитектуру этого взаимодействия, backend, сценарии входящих и исходящих звонков и адаптеры Gemini, OpenAI и xAI.

Сложность проявлялась на стыке компонентов: задержки ответа, перебивания, тишина, разрывы сессий и завершение разговора. Например, голосовая сессия могла закрыться раньше, чем асинхронная задача сохраняла итог звонка. Я воспроизвел проблему, изменил управление задачей и порядок завершения, затем закрепил сценарий тестами.

Для таких расследований я организовал сбор логов одного вызова из нескольких сервисов и проверял исправления реальными SIP-звонками. Параллельно занимался базой знаний, интеграциями, развертыванием и мониторингом. В этом проекте моя ответственность охватывала весь путь от выбора компонентов и проектирования до разбора конкретного сбоя после запуска.

## 33. Вопрос

Есть ли у вас опыт работы с маркетинговыми продуктами и процессами, например с кампаниями, акциями или программами лояльности?

**Ответ:**

Да, мой опыт связан с коммуникациями в маркетинге и продажах. В Aiva я реализовал исходящие кампании: загрузку контактов, расписание с учетом часовых поясов, звонки AI-агента, фиксацию результатов и аналитику. Это позволяет организовать процесс от подготовки списка контактов до просмотра итогов разговоров.

Также я работал над приемом и квалификацией лидов. Агент общается с клиентом, использует базу знаний, сохраняет результат в CRM и при необходимости переводит разговор на сотрудника. В этих сценариях я отвечал за backend, телефонию, логику агента и интеграции с бизнес-системами, включая Bitrix24 и amoCRM.

Механики акций, промокодов и программ лояльности в этом продукте я не разрабатывал. Поэтому наиболее подробно могу рассказать об автоматизации обращений и исходящих коммуникаций, передаче данных в CRM и техническом устройстве кампаний.
