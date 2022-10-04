# Web Closet 👔

1. Start 

        python3 app/log_server.py

        uvicorn app.closet_server:app --reload

1. Run tests:

        python3 app/log_server.py
        
        pytest   
        
   Unit only:

        python3 app/log_server.py

        pytest --without-integration --without-slow-integration

   Integration only:

        python3 app/log_server.py

        pytest app/test/integration_test.py 



1. See the API at http://127.0.0.1:8000/docs

1. Generate summer and winter outfits from your closet 😎
    
    - http://127.0.0.1:8000/randomize/?season=summer
    - http://127.0.0.1:8000/randomize/?season=winter
