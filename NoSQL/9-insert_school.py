#!/usr/bin/env python3
""" 9-insert_school : Insère un nouveau document dans une collection MongoDB """

def insert_school(mongo_collection, **kwargs):
    """
    Insère un nouveau document dans une collection MongoDB en fonction des arguments fournis.

    Args:
        mongo_collection: L'objet collection de pymongo.
        **kwargs: Paires clé-valeur représentant les données du document à insérer.

    Retourne:
        L'_id du document nouvellement inséré.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
