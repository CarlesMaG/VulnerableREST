
users = [
    {
        'id': 'user1',
        'username': 'user1',
        'password': 'user1',
        'mail': 'user1@local.com',
        'role': ''
    },
    {
        'id': 'user2',
        'username': 'user2',
        'password': 'user2',
        'mail': 'user2@local.com',
        'role': 'Doctor'
    },
    {
        'id': 'user3',
        'username': 'user3',
        'password': 'user3',
        'mail': 'user3@local.com',
        'role': 'Auxiliary'
    }
]

patients = [
    {
        'id': 'patient1',
        'name': 'patient1',
        'surname': 'patient1',
        'sensitive_data': 'illness1'
    },
    {
        'id': 'patient2',
        'name': 'patient2',
        'surname': 'patient2',
        'sensitive_data': 'illness2'
    }
]

hospitals = [
    {
        'id': 'hospital1',
        'name': 'hospital1',
        'address': 'fake street 1',
        'phone': '555-55-55-55',
        'departments': [
            {
                'id': 'department1',
                'location': 'building1'
            },
            {
                'id': 'department2',
                'location': 'building2'
            }
        ]
    },
    {
        'id': 'hospital1',
        'name': 'hospital1',
        'address': 'fake street 1',
        'phone': '555-55-55-55',
        'departments': []
    }
]