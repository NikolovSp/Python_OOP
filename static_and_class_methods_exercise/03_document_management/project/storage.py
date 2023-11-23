from typing import List

from project.category import Category
from project.topic import Topic
from project.document import Document


class Storage:
    def __init__(self):
        self.categories: List[Category] = []
        self.topics: List[Topic] = []
        self.documents: List[Document] = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    @staticmethod
    def find_by_id(id: int, place):
        return next((s for s in place if s.id == id), None)

    def edit_category(self, category_id: int, new_name: str):
        category = self.find_by_id(category_id, self.categories)
        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.find_by_id(topic_id, self.topics)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.find_by_id(document_id, self.documents)
        document.edit(new_file_name)

    def delete_category(self, category_id: int):
        category = self.find_by_id(category_id, self.categories)
        self.categories.remove(category)

    def delete_topic(self, topic_id: int):
        topic = self.find_by_id(topic_id, self.topics)
        self.topics.remove(topic)

    def delete_document(self, document_id: int):
        document = self.find_by_id(document_id, self.documents)
        self.documents.remove(document)

    def get_document(self, document_id: int):
        document = self.find_by_id(document_id, self.documents)
        return document

    def __repr__(self):
        return '\n'.join([d.__repr__() for d in self.documents])
