For this project, I created a Polyglot Persistence Application, which uses multiple types of databases (SQL & NoSQL) within the same system, allowing them to talk to each other seamlessly.

1. First, I accessed the provided database, built tables, defined relationships, and populated them using VSCode (see the 'Initial Setup' file).
2. Once my teammate created the NoSQL side of the application, I opened Jupyter Notebook and wrote a block of code to establish secure connections to both SQL and NoSQL databases using a password.
3. Through careful and iterative prompting, I developed a user-friendly, fault-tolerant interface that accesses both databases and performs basic CRUD operations.
4. I then created two advanced query runners that allow for structural changes (e.g. adding new tables).
5. I also included a bulk importer to make it easy to add large volumes of data efficiently.
6. Lastly, I performed a brief data analysis and built a simple machine learning model that predicts monthly income based on employee attributes.
