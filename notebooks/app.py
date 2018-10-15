from flask import Flask, request
from sklearn.feature_extraction.text import CountVectorizer
import re
import pickle

# regular expressions
REPLACE_NO_SPACE = re.compile("(\.)|(\;)|(\:)|(\!)|(\')|(\?)|(\,)|(\")|(\()|(\))|(\[)|(\])")
REPLACE_WITH_SPACE = re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)")

# load vectorization model
pickle_file = open('models/cv_pickle', 'rb')
cv = pickle.loads(pickle_file.read())

# load ML model
pickle_file = open('models/final_model', 'rb')
final_model = pickle.loads(pickle_file.read())


# prepare input to be classified
def prepare_input(review):
    review = REPLACE_NO_SPACE.sub("", review.lower())
    review = REPLACE_WITH_SPACE.sub(" ", review)

    return cv.transform([review])


app = Flask(__name__)

@app.route('/api/v1.0/scorefy', methods=["GET"])
def scorefy():
    query_parameters = request.args
    review = query_parameters.get('r')
    return final_model.predict(prepare_input(review))[0]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
