
test:
	   for t in *.in; do python3 iterative.py $$t > sortida; diff -q `basename $$t .in`.pa.ans sortida; done #en aqueducte.py s'ha de ficar el arxiu que es desitgi (recursive.py or iterative.py)
	    
