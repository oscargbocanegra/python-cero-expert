# Single Responsibility Principle (SRP) in Python

<table>
<colgroup>
<col width="30%" />
<col width="30%" />
<col width="40%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: center;"><strong>Definition</strong></th>
<th style="text-align: center;"><strong>Benefits</strong></th>
<th style="text-align: center;"><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>"A class should have one, and only one, reason to change."</strong> <br><br> The SRP states that a class should have only one responsibility and should encapsulate only one reason for change. This principle helps create more maintainable, testable, and understandable code. <br><br> <strong>Key Concepts:</strong> <br> • Focus on a single responsibility <br> • One reason to change <br> • Separation of concerns <br> • Clear and defined purpose</td>
<td>• <strong>Easier to understand</strong>: Classes with single responsibility are simpler to comprehend and reason about <br><br> • <strong>Easier to maintain</strong>: Changes to one responsibility don't affect others, reducing side effects <br><br> • <strong>Easier to test</strong>: Focused classes are easier to unit test with fewer dependencies <br><br> • <strong>Reduced coupling</strong>: Classes are less dependent on each other, improving modularity <br><br> • <strong>Better organization</strong>: Code is more organized and structured, improving readability <br><br> • <strong>Reusability</strong>: Single-purpose classes can be reused in different contexts <br><br> • <strong>Debugging</strong>: Easier to locate and fix bugs when responsibilities are clearly separated</td>
<td>

```python
# ❌ Violates SRP
class User: 
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def save_to_database(self):
        pass  # Database logic
    def send_email(self):
        pass  # Email logic


# ✅ Follows SRP
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:
    def save(self, user):
        pass  # Database logic

class EmailService:
    def send_email(self, user):
        pass  # Email logic
```
</td>
</tr>
</tbody>
</table> 