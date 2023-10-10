class ChemVecDbResource:
    def to_resource(self):
        return {"type": "dsvecdb", "instance_id": "chem_vecdb"}


class KnowledgeDbResource:
    def to_resource(self):
        return {"type": "db", "instance_id": "knowledge_db"}
