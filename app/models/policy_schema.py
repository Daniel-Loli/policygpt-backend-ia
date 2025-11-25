policy_schema = {
    "name": "extract_policy",
    "description": "Extrae información estructurada de una póliza de seguro",
    "parameters": {
        "type": "object",
        "properties": {
            "coverages": {"type": "array", "items": {"type": "string"}},
            "exclusions": {"type": "array", "items": {"type": "string"}},
            "deductibles": {"type": "string"},
            "special_conditions": {
                "type": "array", 
                "items": {"type": "string"}
            },
            "summary": {"type": "string"}
        },
        "required": ["coverages", "exclusions", "summary"]
    }
}
