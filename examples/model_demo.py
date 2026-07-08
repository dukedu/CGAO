from cgao.models import *

post = Post()

author = Author(

    author_id="123",

    nickname="Duke"

)

result = DetailResult(

    post=post,

    author=author

)

print(result)