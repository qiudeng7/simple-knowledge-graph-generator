from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from KnowledgeGraph import KnowledgeGraph

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/show")
async def redirect_to_new_path():
    return RedirectResponse(url="/static/show/index.html")

@app.get("/assets/index-C1uoPy3x.js")
async def redirect_to_new_path():
    return RedirectResponse(url="/static/assets/index-C1uoPy3x.js")
@app.get("/assets/index-B_RRt6cs.css")
async def redirect_to_new_path():
    return RedirectResponse(url="/static/assets/index-B_RRt6cs.css")


@app.get("/")
async def redirect_to_new_path():
    return RedirectResponse(url="/static/index.html")


class Item(BaseModel):
    text: str


@app.post("/knowledge-graph/")
async def create_knowledge_graph(data: Item):
    if data.text == "刘姥姥进大观园":
        cache = [{"entities":{"贾母":"人物"},"relation":None},{"entities":{"刘姥姥":"人物"},"relation":None},{"entities":{"凤姐":"人物"},"relation":None},{"entities":{"潇湘馆":"网络小说","池中":"人物"},"relation":"主角"},{"entities":{"贾母":"人物"},"relation":None},{"entities":{"菱":"歌曲"},"relation":None},{"entities":{"王夫人":"人物"},"relation":None},{"entities":{"贾母":"人物","三":"人物"},"relation":"妻子"},{"entities":{"凤":"网络小说"},"relation":None},{"entities":{"鸳鸯":"人物","咱":"电视综艺"},"relation":"主演"},{"entities":{"咱":"人物","女客":"人物"},"relation":"父亲"},{"entities":{"李纨":"人物","刘姥姥":"人物"},"relation":"父亲"},{"entities":{"李纨笑":"人物"},"relation":None},{"entities":{"鸳鸯":"人物"},"relation":None},{"entities":{"贾母":"人物","凤姐":"人物"},"relation":"母亲"},{"entities":{"贾母":"人物","刘亲":"人物"},"relation":"母亲"},{"entities":{"凤姐":"人物","鸳鸯":"人物","刘姥姥":"人物"},"relation":"妻子"},{"entities":{"调":"歌曲","然后":"歌曲","归坐":"人物"},"relation":"歌手"},{"entities":{"薛姨妈":"人物"},"relation":None},{"entities":{"贾母":"人物","王夫人":"人物"},"relation":"妻子"},{"entities":{"贾母":"人物","鸳鸯":"人物"},"relation":"母亲"},{"entities":{"丫鬟们":"人物","刘姥姥":"人物"},"relation":"妻子"},{"entities":{"鸳鸯":"歌曲","侍":"人物"},"relation":"歌手"},{"entities":{"刘姥姥":"人物"},"relation":None},{"entities":{"刘姥姥":"人物","凤姐":"人物","鸳鸯":"人物"},"relation":"父亲"},{"entities":{"刘姥姥":"人物"},"relation":None},{"entities":{"李纨":"人物","贾":"人物","凤姐":"人物"},"relation":"父亲"},{"entities":{"贾母":"人物","刘姥姥":"人物"},"relation":"母亲"},{"entities":{"湘云掌":"歌曲","茶":"歌曲"},"relation":"所属专辑"},{"entities":{"贾母":"人物","王夫人":"人物"},"relation":"母亲"},{"entities":{"薛姨妈":"人物"},"relation":None},{"entities":{"探春":"歌曲","迎春":"歌曲"},"relation":"所属专辑"},{"entities":{"惜春":"人物","揉揉肠子":"人物"},"relation":"母亲"},{"entities":{"地下无":"人物"},"relation":None},{"entities":{"凤姐":"人物","鸳鸯":"人物","刘姥姥":"人物"},"relation":"妻子"},{"entities":{"刘姥姥":"人物","鸡儿":"歌曲"},"relation":"歌手"},{"entities":{"我":"歌曲","且得":"歌曲","一个儿":"歌曲"},"relation":"歌手"},{"entities":{"贾母":"人物","琥珀":"人物"},"relation":"母亲"},{"entities":{"贾母":"人物","凤丫头":"人物"},"relation":"母亲"},{"entities":{"刘姥姥":"人物","鸡蛋":"人物","凤姐儿":"人物"},"relation":"父亲"},{"entities":{"刘姥姥":"人物"},"relation":None},{"entities":{"地":"歌曲"},"relation":None},{"entities":{"刘姥姥":"人物","一两银子":"歌曲"},"relation":"歌手"},{"entities":{"众":"歌曲","已":"歌曲","没心":"歌曲","取":"歌曲"},"relation":"歌手"},{"entities":{"贾母":"人物","凤丫头":"人物"},"relation":"父亲"},{"entities":{"凤姐":"人物","鸳鸯":"人物"},"relation":"妻子"},{"entities":{"刘姥姥":"人物"},"relation":None},{"entities":{"凤姐儿":"人物"},"relation":None},{"entities":{"刘姥姥":"人物"},"relation":None},{"entities":{"贾母":"人物"},"relation":None},{"entities":{"老嬷":"人物","板儿":"人物"},"relation":"父亲"},{"entities":{"贾母":"人物","探春":"人物"},"relation":"母亲"},{"entities":{"刘姥":"人物","李纨":"人物","凤姐儿":"人物"},"relation":"妻子"},{"entities":{"凤姐儿":"人物"},"relation":None},{"entities":{"鸳鸯":"人物"},"relation":None},{"entities":{"刘姥姥":"人物"},"relation":None},{"entities":{"我要恼":"歌曲"},"relation":None},{"entities":{"鸳鸯":"人物","刘姥姥":"人物"},"relation":"父亲"},{"entities":{"凤姐儿":"人物","鸳鸯":"人物"},"relation":"父亲"},{"entities":{"鸳鸯":"人物","碗箸":"人物"},"relation":"父亲"}]
        return cache
    else:
        kg = KnowledgeGraph(data.text)
        return kg.triples

origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
