
==========================================================
Cards functionality
==========================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Card's models
========================================
.. automodule:: cards.models
.. autoclass:: EnglishCards
   :members:
   :show-inheritance:
.. autoclass:: CardsCollections
   :members:
   :show-inheritance:


Card's forms
========================================
.. automodule:: cards.forms

.. autoclass:: CardForm
   :members:
   :show-inheritance:

.. autoclass:: CollectionForm
   :members:
   :show-inheritance:


Card's views
========================================
.. automodule:: cards.views.card_views
.. autoclass:: CardsListView
   :members:
   :undoc-members:
.. autoclass:: CreateCardView
   :members:
   :undoc-members:
.. autoclass:: CardDeleteView
   :members:
   :undoc-members:
.. automodule:: cards.views.collection_views
.. autoclass:: CollectionListView
   :members:
   :undoc-members:
.. autoclass:: CollectionCreateView
   :members:
   :undoc-members:
.. autoclass:: CollectionDeleteView
   :members:
   :undoc-members:
.. autoclass:: CollectionEditView
   :members:
   :undoc-members:
.. autoclass:: CollectionRenameView
   :members:
   :undoc-members:
.. automodule:: cards.views.main
.. autofunction:: main

Card's services
========================================
.. automodule:: cards.services.abstract_class
.. autoclass:: MessageMixin
   :members:
   :undoc-members:
.. automodule:: cards.services.cards_services
.. autoclass:: CardsServices
   :members:
   :undoc-members:
.. automodule:: cards.services.collections_services
.. autoclass:: CollectionServices
   :members:
   :undoc-members:
.. automodule:: cards.services.fact_generator
.. autofunction:: fact_generator
.. automodule:: cards.services.translator
.. autofunction:: translator