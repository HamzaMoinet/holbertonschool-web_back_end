#!/usr/bin/env python3
"""Module qui met à jour les sujets d'un document d'école par son nom."""


def update_topics(mongo_collection, name, topics):
    """
    Modifie tous les sujets (topics) d'un document d'école en fonction du nom.

    Args:
        mongo_collection: L'objet collection de pymongo.
        name (str): Le nom de l'école à mettre à jour.
        topics (list): Liste des sujets (topics) à définir pour l'école.

    Retourne:
        None
    """
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
