from keras.models import Model
from keras.layers import Dense, Dropout, LSTM, Input, Activation
from keras import optimizers

def buildModelFinance(backcandles, data_set):
    lstm_input = Input(shape=(backcandles, data_set.shape[1]), name='lstm_input')
    x = LSTM(150, return_sequences=True)(lstm_input)
    x = Dropout(0.3)(x)
    x = LSTM(150)(x)
    x = Dropout(0.3)(x)
    x = Dense(50, activation='relu')(x)
    x = Dense(1)(x)
    output = Activation('linear', name='output')(x)
    model = Model(inputs=lstm_input, outputs=output)
    adam = optimizers.Adam(learning_rate=0.0005)
    model.compile(optimizer=adam, loss='mse')
    return model

def trainModelFinance(model, X_train, y_train, epochs=30, batch_size=20, validation_split=0.1, shuffle=True):
    model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_split=validation_split, shuffle=shuffle)
    return model

def predictValueFinance(model, X_test):
    p = model.predict(X_test)
    return p
