# Remediation for FIREBASE_UNAUTHENTICATED

## Remediation Steps for Firebase Collection Exposed Data 
Firebase Collection exposing data to the public is a serious security issue. Without proper rules, attackers can gain unauthorized access to your database and can even modify your data.

**Step 1: Restrict Access to authorized users only**

In your firebase rules, restrict the access to your collections to only authorized users. This is done by checking the authenticated user's uid against the request.auth.uid.

```json
{
  "rules": {
    "your_collection": {
      "$uid": {
        ".read": "auth != null && auth.uid == $uid",
        ".write": "auth != null && auth.uid == $uid"
      }
    }
  }
}
```
**Step 2: Use Firebase Security Rules to your advantage**

Firebase Security Rules allow you to control access to data stored in different Firebase products. You can write rules to control read and write operations from your Firebase Realtime database or Firestore database, for example.

Sample Validation rule (Firestore):

```json
{
  "rules": {
    "your_collection": {
      ".read": "auth != null",
      ".write": "auth != null"
    }
  }
}
```
**Step 3: Regularly review your rules**

Regularly review your Firebase Security Rules in order to avoid unwanted-exposed data. Remember that new collections do not automatically inherit the rules of their parent/root collection.

```bash
firebase deploy --only firestore:rules
```
**Step 4: Store sensitive information securely**

Use Firebase Cloud Functions or your own server to handle logic involving sensitive information behind your own server's security.

```js
const functions = require('firebase-functions');
const admin = require('firebase-admin');
admin.initializeApp();

exports.yourFunctionName = functions.https.onCall((data, context) => {
    // your server side logic goes here
});
```
Remember that no single rule works in all scenarios. Therefore, write your rules to fit the needs of your specific app.