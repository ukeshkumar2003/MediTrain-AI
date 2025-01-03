@app.route("/response", methods=["POST"])
def response():
    try:
        data = request.get_json()
        query = data.get("query")
        response = get_response(query)
        return jsonify({"response": response})
    except Exception as e:
        print(e)
        return jsonify({"error": str(e)}), 500

if _name_ == "_main_":
    # app.run(debug=True)
    app.run(host="0.0.0.0")
