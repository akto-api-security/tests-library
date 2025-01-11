# Remediation for GOOGLE_API_KEY_DISCLOSURE

## Remediation Steps for Google API Key Disclosure

Google API Key Disclosure is a serious security breach. It occurs when your unique API Key that you generate to use Google's APIs (like Google Maps, Google Analytics, Google Cloud etc.) is exposed publicly, leading to potentially unauthorized usage and abuse of resources.

**Note:** The steps below will help you secure your Google API keys however, you should make sure any existing exposed keys are revoked and new keys generated following the steps below.

### Step 1: Regenerate API Key:

You need to go your Google Cloud Console to regenerate an API Key.

```java
Go to the 'Credentials' page in the Google Cloud Console.
Select the project containing the API key you want to edit.
Click on the name of the existing API key that you want to secure.
Click on 'Regenerate key' and then click the 'Regenerate' button in the panel that appears.
```

### Step 2: Secure your API Key

After regenerating your key, always store it serverside and only expose what is necessary on the client side. 

For the server side if you use NODE.JS for your backend, you can store your new API Key in a `.env` file and use the `dotenv` package to access it. 

```javascript
// After installing dotenv with npm install dotenv
require('dotenv').config()

const apiKey = process.env.YOUR_GENERATED_API_KEY;
```

Don't forget to add `.env` to your `.gitignore` file.

### Step 3: Restrict Usage

Prevent unauthorized access by restricting how your API key can be used. Just navigate to the API console and set the website that is allowed to use this key.

```java
Go to the 'Credentials' page in the Google Cloud Console.
Select the project containing the API key you want to edit.
Click on the name of the existing API key that you want to secure.
Under 'Key restrictions', choose 'HTTP referrers (websites)'.
Then under 'Accept requests from these HTTP referrers (websites)', add the websites that you want to restrict your API to.
```