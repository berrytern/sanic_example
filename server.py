from sanic import Sanic, request
from sanic.response import text, json
app = Sanic("MyHelloWorldApp")

users = []

# declaração das rotas
@app.get("/users")
async def buscar_users(request: request):
    return json(users)

@app.get("/users/<id:int>")
async def buscar_user_by_id(request: request, id):
    for user in users:
        if user["id"] == id:
            return json(user)
    return text("Not Found")


@app.post("/users")
async def create_user(request: request):
    users.append(request.json)
    return json(request.json)


@app.patch("/users/<id:int>")
async def update_user(request: request, ):
    index = 0
    for user in users:
        if user["id"] == id:
            users[index] = request.json
            return json(user)
        index+=1
    return json(users)

@app.delete("/users/<id:int>")
async def delete_user(request: request, id):
    index = 0
    for user in users:
        if user["id"] == id:
            users.pop(index)
        index+=1

    return text("deleted")

# começar a servir a aplicação
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)