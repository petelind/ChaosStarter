**This example is based on the book by (c) Russ Miles "Learning Chaos Engineering", chapter 5.**

###### How do I prep my environment?
1. Install python 3.X if you dont already have it.
2. Create a virtual environment: 
python3 -m venv ~/.venvs/chaostk
`source ~/.venvs/chaostk/activate`
3. Install Chaos Toolkit:
`pip install chaostoolit`
4. Type chaos --versiob to make sure everything is allright.

###### How do I run the experiment which invalidates steady state hypothesis?
1. Start the service:
`python3 service.py &`
2. Run the experiment:
`chaos run experiment.json`
3. See it failing.

###### How do I run the experiment which proves that the service is resilient, eg complies steady state hypothesis?
1. Start the service:
`python3 resilient-service.py &`
2. Run the experiment:
`chaos run experiment.json`
3. See it succeeding.

