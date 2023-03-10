import pickle
import streamlit as st 


pickle_in = open("BankNote.pickle","rb")
classifier=pickle.load(pickle_in)


def predict_note_authentication(variance,skewness,curtosis,entropy):
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction

def main():
    st.title("Bank Note Authentication Classification")
    Variance = st.text_input("Variance")
    Skewness = st.text_input("skewness")
    Curtosis = st.text_input("curtosis")
    Entropy = st.text_input("entropy")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))
    

if __name__=='__main__':
    main()
    
    
    
