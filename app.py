from flask import Flask,request,  render_template
from free import TextSimilarity
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/predict',methods=['POST'])
def predict(stop_usage =1):
    texts = [x for x in request.form.values()]

    first = TextSimilarity(texts[0].lower().strip())
    second = TextSimilarity(texts[1].lower().strip())
    third = TextSimilarity(texts[2].lower().strip())
    stop_usage = int(texts[3])

    first.create_tokens()
    second.create_tokens()
    third.create_tokens()

    first.remove_stop_words(stop_usage)
    second.remove_stop_words(stop_usage)
    third.remove_stop_words(stop_usage)

    print(first.cleaned_tokens)
    print(second.cleaned_tokens)
    print(third.cleaned_tokens)

    first_second_similarity = first.cosine_similar_score(second)
    second_third_similarity = second.cosine_similar_score(third)
    first_third_similarity = first.cosine_similar_score(third)
    result = f'first --> Second {round(first_second_similarity,3)   }   '+ \
            f'   Second --> Third {round(second_third_similarity,3) }   ' + \
            f'   First --> Third  {round(first_third_similarity,3)  }'
    return render_template('home.html',result=result)

if __name__ == '__main__':
    app.run(debug=True)
