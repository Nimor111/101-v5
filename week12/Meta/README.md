# Python Serializer

We are going to implement a simple serializer with declarative way of describing fields.

Serializer should take a instance of python object and turn it into a dictionary, that can be passed to `json.dumps` without any problems.

This is what we are looking for:

```python
class Comment(object):
    def __init__(self, email, content, created_at=None):
        self.email = email
        self.content = content

        if created_at is None:
            created_at = datetime.now()

        self.created_at = created_at


class CommentSerializer(Serializer):
    email = EmailField()
    content = CharField()
    created_at = DateTimeField()

comment = Comment(email='radorado@hakbulgaria.com', content='wie naistina li hakvate?')
serializer = CommentSerializer(comment)

print(serializer.is_valid()) # True
print(serializer.data)
"""
{
  "email": "radorado@hackbulgaria.com",
  "content": "wie naistina li hakvate?",
  "created_at": "'2017-01-20T13:43:10.704846'"
}
"""
```

Our serializer should support only two methods:

* `.is_valid()` - returns `True` if the passed data is valid according to the fields. For example, if we pass `123` to the `email` field, this should not be valid.
* `.data` - returns the desired dictionary. You can call `.data` only if the serializer is valid (a call to `.is_valid()` has been made before that)

