# Remediation for IMPROPER_INPUT_IN_KAFKA_REST

## Remediation Steps for Improper Input Validation in Kafka-REST

Improper input validation in Kafka-REST could lead to unpredictable and detrimental behavior in the software, potentially even security vulnerabilities. Promptly addressing these issues is essential.

### Step 1: Validate All User Input

All user input must be validated to ensure it does not carry malicious payloads. It would be best if you used a robust, well-maintained validation software, like Kafka's Streams API. The following Scala example demonstrates a simple usage:

```scala
import org.apache.kafka.streams.kstream.Predicate

val isNotNull: Predicate[String, String] = new Predicate[String, String] {
  override def test(key: String, value: String): Boolean = {
    key != null && value != null
  }
}
```

### Step 2: Sanitize All User Input

Sanitize user input before sending it to any API or database. Avoid raw user input as it may expose the application to injection attacks.

```java
import org.apache.commons.lang3.StringEscapeUtils;

public String sanitize(String input) {
    return StringEscapeUtils.escapeJava(input);
}
```