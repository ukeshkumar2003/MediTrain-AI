from flask import Flask, jsonify, request

app = Flask(_name_)

# Sample training content data
training_modules = [
    {
        "id": 1,
        "title": "Introduction to Anatomy",
        "description": "Basic concepts of human anatomy and its applications.",
        "duration": "30 minutes",
        "level": "Beginner"
    },
    {
        "id": 2,
        "title": "Advanced Cardiovascular Procedures",
        "description": "Detailed procedures and protocols for handling cardiovascular emergencies.",
        "duration": "1 hour",
        "level": "Advanced"
    },
]

# API to fetch all training modules
@app.route('/api/content', methods=['GET'])
def get_all_content():
    return jsonify({"status": "success", "modules": training_modules}), 200

# API to fetch a specific module by ID
@app.route('/api/content/<int:module_id>', methods=['GET'])
def get_content_by_id(module_id):
    module = next((item for item in training_modules if item["id"] == module_id), None)
    if module:
        return jsonify({"status": "success", "module": module}), 200
    else:
        return jsonify({"status": "error", "message": "Module not found"}), 404

# API to add a new training module
@app.route('/api/content', methods=['POST'])
def add_content():
    new_module = request.json
    new_module["id"] = len(training_modules) + 1
    training_modules.append(new_module)
    return jsonify({"status": "success", "message": "Module added", "module": new_module}), 201

# Run the app
if _name_ == '_main_':
    app.run(debug=True)
