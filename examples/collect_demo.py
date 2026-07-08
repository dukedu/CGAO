from cgao.services import Pipeline

pipe = Pipeline()

posts = pipe.collect(

    keyword="DeepSeek",

    limit=50,

    csv="data/raw/DeepSeek.csv",

    json="data/raw/DeepSeek.json",

)

print()

print(f"Collected : {len(posts)}")