from flask import Flask, jsonify

app = Flask(__name__)

# 模拟一些用户数据
users = {
    "1": {"name": "Alice", "email": "alice@example.com"},
    "2": {"name": "Bob", "email": "bob@example.com"},
}

# 用户信息查询接口
@app.route("/api/users/<user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# 健康检查接口
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    # 监听 0.0.0.0 确保容器中可访问
    app.run(host="0.0.0.0", port=5000)
