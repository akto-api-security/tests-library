

## Remediation Steps for Time-Based SQL Injection in SQLite DB

Time-based SQL injection is a serious security flaw that can allow an attacker to execute malicious SQL statements on your database, potentially leading to data breaches or other serious problems.

### Step 1: Use Prepared Statements
The first and most effective way is to use prepared statements with parameterized queries. Most development languages support this feature.

If we're working with Node.js, the SQLite driver supports prepared statements:

```javascript
const sqlite3 = require('sqlite3').verbose();
let db = new sqlite3.Database(':memory:');

let param = '1';
db.run(`INSERT INTO langs(name) VALUES(?)`, [param], function(err) {
  if (err) {
    return console.error(err.message);
  }
  console.log(`A row has been inserted with rowid ${this.lastID}`);
});
db.close();
```

### Step 2: Employ Escaping All User Supplied Input
Most development languages support this feature either directly or via third-party libraries. This ensures that all user-submitted data is safe to use in a SQL query.

With Node.js, for example:

```javascript
const sqlite3 = require('sqlite3').verbose();
let db = new sqlite3.Database(':memory:');

let rawInput = "user input";
let escapedInput = sqlite3.escape(rawInput); // Escape user input

db.run(`SELECT * FROM table WHERE column = '${escapedInput}'`);
db.close();
```

Please note that SQLite3 does not have built-in `escape` method. Please use corresponding escape methods depending on your application language.

### Step 3: Employ an Application Firewall
An application firewall can spot and block SQL injection attempts. Some platforms have built-in support for this, while others loose support via extensions.