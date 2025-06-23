train_data = prices[:1000]
test_data = prices[1000:]
def Adaptive_ARMA(train_data, test_data, lr):
    phi = 0.5
    theta = 0.5
    predictions = []

    yt = train_data.iloc[-1]
    e = 0            

    for actual in test_data:
      
        ycap = phi * yt + theta * e
        predictions.append(ycap)

   
        error = actual - ycap
        phi += lr * error * yt
        theta += lr * error * e

        yt = actual
        e = error

    return predictions

predictions = Adaptive_ARMA(train_data,test_data,0.00001)
