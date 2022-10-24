import pytest
from unittest.mock import patch
from app import documents, directories, check_document_existance, get_doc_owner_name, remove_doc_from_shelf, delete_doc


@patch('builtins.input', return_value="10006")
def test_get_doc_owner_name(mock_input):
    result = get_doc_owner_name()
    assert result == "Аристарх Павлов"

def test_remove_doc_from_shelf():
    start_values = directories['2'].copy()
    remove_doc_from_shelf('10006')
    finish_values = directories['2'].copy()
    assert '10006' in start_values and '10006' not in finish_values

@patch('builtins.input', return_value="10006")
def test_delete_doc(mock_input):
    start_values = documents[2]['number']
    delete_doc()
    finish_values = 'OK'
    for doc in documents:
        if doc['number'] == '10006':
            finish_values = 'NOT OK'
    assert '10006' in start_values and finish_values == 'OK'
