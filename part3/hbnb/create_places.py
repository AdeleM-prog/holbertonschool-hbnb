#!/usr/bin/python3
"""Script to create sample Place records in the HBnB application."""

from app import create_app, db
from app.services.facade import HBnBFacade

DEFAULT_USER = {
    'first_name': 'Demo',
    'last_name': 'Owner',
    'email': 'demo.owner@example.com',
    'password': 'password123',
}

PLACES_TO_CREATE = [
    {
        'title': 'Appartement cosy au centre-ville',
        'description': 'Charmant appartement avec vue sur la place principale.',
        'price': 79.99,
        'latitude': 48.8566,
        'longitude': 2.3522,
    },
    {
        'title': 'Loft moderne près du parc',
        'description': 'Grand loft lumineux, idéal pour un week-end en famille.',
        'price': 120.00,
        'latitude': 48.8638,
        'longitude': 2.3499,
    },
    {
        'title': 'Studio calme en bordure de rivière',
        'description': 'Studio cosy, parfait pour les voyageurs solos.',
        'price': 10.00,
        'latitude': 48.8606,
        'longitude': 2.3376,
    },
]


def main():
    app = create_app()

    with app.app_context():
        db.create_all()

        facade = HBnBFacade()

        owner = facade.get_user_by_email(DEFAULT_USER['email'])
        if owner is None:
            owner = facade.create_user(DEFAULT_USER)
            print(f"Utilisateur créé: {owner.email} (id={owner.id})")
        else:
            print(f"Utilisateur existant trouvé: {owner.email} (id={owner.id})")

        created_places = []
        for place_info in PLACES_TO_CREATE:
            place_data = place_info.copy()
            place_data['owner_id'] = owner.id
            try:
                place = facade.create_place(place_data)
                created_places.append(place)
                print(f"Place créée: {place.title} (id={place.id})")
            except Exception as exc:
                print(f"Erreur lors de la création de '{place_data['title']}': {exc}")

        print('\nRésumé:')
        print(f"Total des places tentées: {len(PLACES_TO_CREATE)}")
        print(f"Places créées: {len(created_places)}")


if __name__ == '__main__':
    main()
