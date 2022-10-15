'''
Question Sınıfı
Question sınıfı ile her bir soruyu temsil edecek olan bir nesne oluşturma imkanına sahip oluyoruz.

class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    def checkAnswer(self, answer):
        return self.answer == answer
Her bir soru için text (soru), choices (şıklar) ve answer (doğru olan cevap) şeklinde özelliklerimiz mevcut.

Her soru için bir Question sınıfından türetilmiş bir nesneye ihtiyacımız var ve oluşturulacak test 5 sorudan oluşuyorsa bu durumda 5 tane Question nesnesi bir liste içinde barındırılmalıdır.

q1 = Question('en iyi programlama dili hangisidir ?', ['C#','python','javascript','java'], 'python')
q2 = Question('en popüler programlama dili hangisidir ?', ['python','javascript','C#','java'], 'python')
q3 = Question('en çok kazandıran programlama dili hangisidir ?', ['C#','javascript','java','python'], 'python')
q4 = Question('en çok sevilen programlama dili hangisidir ?', ['C#','javascript','java','python'], 'python')
q5 = Question('en kolay programlama dili hangisidir ?', ['C#','javascript','java','python'], 'python')

questions = [q1,q2,q3,q4,q5]
Quiz Sınıfı
Soru listesini kullanıcıya sırayla gösterecek ve verilen cevaba göre skor bilgisini tutacak özellikler ve gerekli metotları içerecek olan bir Quiz sınıfı oluşturuyoruz.

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0
Quiz sınıfından türetilecek olan her bir nesne bir kullanıcı için başlatılacak olan bir quizi temsil eder. 

quiz = Quiz(questions)
Quiz sınıfına soru listesini veriyoruz. 

score bilgisi başlangıçta 0 ve questionIndex ise ilk soruyu temsil ediyor yani questions listesinin questions[questionIndex] eleman bize ilk soruyu verir ve sonraki soru için questionIndex bilgisinin 1 arttırır bir önceki soru için ise 1 azatmamız gerekir bu şekilde sorular arasında ilerleyebiliriz.

class Quiz:

    # diğer tanımlamalar...

    def getQuestion(self):
       return self.questions[self.questionIndex]
Quiz sınıfı içinde tanımlı questions listesindeki her bir soruyu almak için getQuestion() metodunu kullanabiliriz burada önemli olan questionIndex bilgisinin kaç olduğudur.

getQuestion() metodunu tek başına çağırmak yerine başka bir metot içerisinden çağıracağız.

def displayQuestion(self):
    question = self.getQuestion()
    print(f'Soru {self.questionIndex + 1}: {question.text}')

    for q in question.choices:
        print('-'+ q)
        
    answer = input('cevap: ')
    self.guess(answer)
    self.loadQuestion()
self.getQuestion() dediğimizde o anda Quiz nesnesi içindeki questionIndex bilgisine göre aktif soru karşımıza gelir ve sorunun cevap şıklarını ise question.choices içinden alıyoruz. Şıklar yazıldıktan sonra kullanıcının cevabını alıp guess(answer) metoduna gönderiyoruz.

def guess(self, answer):
    question = self.getQuestion()
    if question.checkAnswer(answer):
       self.score += 1
       self.questionIndex += 1
guess() metodu içerisinde ise tekrar aktif Question nesnesine ulaşıp nesne üzerinden sorunun cevabını checkAnswer() metodunu ile kondrol ediyoruz. Gelen cevap true ise score bilgisini 1 arttırıp sonrasi soruya geçmek için questionIndex bilgisini 1 arttırıyoruz.

self.guess(answer)
self.loadQuestion()
guess() metodunun hemen arkasından loadQuestion() metodu çağrılıyor.

def loadQuestion(self):
    if len(self.questions) == self.questionIndex:
        self.showScore()
     else:         
        self.displayProgress()  
        self.displayQuestion()
eğer ki soru sayısı eğer ki questionIndex değerine eşitse bu durumda kullanıcıya score bilgisini gösterip quiz' i bitiriyoruz.

def showScore(self):
     print('score: ', self.score)
Eğer ki halen gösterilecek soru varsa bu durumda displayProgress() metodunu çağırıp quiz' deki ilerlemeyi gösteriyoruz ve sonraki soruya geçiş yapıyoruz.

def displayProgress(self):
     totalQuestion = len(self.questions)
     questionNumber = self.questionIndex + 1

     if questionNumber > totalQuestion:
         print('Quiz bitti.')
     else:
         print(f'Question {questionNumber} of {totalQuestion}'.center(100,'*'))
Son olarak uygulamayı başlatmak için ise loadQuestion() metodunu kullanıyoruz.

quiz.loadQuestion()
Quiz Uygulamasının Son Hali
# Question
class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer
    
    def checkAnswer(self, answer):
        return self.answer == answer

# Quiz
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.questionIndex + 1}: {question.text}')

        for q in question.choices:
            print('-'+ q)
        
        answer = input('cevap: ')
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:         
            self.displayProgress()  
            self.displayQuestion()

    def showScore(self):
        print('score: ', self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print('Quiz bitti.')
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(100,'*'))

q1 = Question('en iyi programlama dili hangisidir ?', ['C#','python','javascript','java'], 'python')
q2 = Question('en popüler programlama dili hangisidir ?', ['python','javascript','C#','java'], 'python')
q3 = Question('en çok kazandıran programlama dili hangisidir ?', ['C#','javascript','java','python'], 'python')
q4 = Question('en çok sevilen programlama dili hangisidir ?', ['C#','javascript','java','python'], 'python')
q5 = Question('en kolay programlama dili hangisidir ?', ['C#','javascript','java','python'], 'python')

questions = [q1,q2,q3,q4,q5]
quiz = Quiz(questions)

quiz.loadQuestion()
'''