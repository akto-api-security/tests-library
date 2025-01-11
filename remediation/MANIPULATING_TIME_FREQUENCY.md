# Remediation for MANIPULATING_TIME_FREQUENCY

## Remediation Steps for Manipulating Time Frequency
Manipulation of the system time frequency can lead to a variety of security issues. It might allow attackers to interfere with time-dependent functionalities or manipulate the outputs of a system.

### Step 1: Use Time API's instead of System Clock
Use the time API's specific to the language you are coding in. Do not rely on the system clock for time tracking within your application.

```java
//Java Example
long millis = System.currentTimeMillis(); 
```

```python
#Python Example
import time
millis = int(round(time.time() * 1000))
```

### Step 2: Validate Time Period
If specific functionalities in your application are time-dependent, make sure you are validating that the time elapsed is within an acceptable range.

```java
//Java Example
final long MAX_DIFFERENCE = 1000;
long startTime = System.currentTimeMillis();
//... perform task
long endTime = System.currentTimeMillis();
if (endTime - startTime > MAX_DIFFERENCE) {
  throw new RuntimeException("Task took too long!");
}

```

### Step 3: Use Secure NTP (Network Time Protocol) 
Use secure NTP to synchronize time across machines in the network. This minimizes the chance of a potential attacker manipulating the time frequency.

```bash
#Install NTP
sudo apt-get install ntp
#Edit the NTP configuration file
sudo nano /etc/ntp.conf
#Add server pool.ntp.org iburst, then save and exit
#Restart the NTP service
sudo service ntp restart
```