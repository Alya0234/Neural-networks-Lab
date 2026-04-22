import tensorflow as tf
from tensorflow.keras import layers, models

# Load dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train = x_train / 255.0
x_test = x_test / 255.0

x_train = x_train.reshape(-1,28,28,1)
x_test = x_test.reshape(-1,28,28,1)

def build_model(optimizer):
    model = models.Sequential([
        layers.Conv2D(16, (3,3), activation='relu', input_shape=(28,28,1)),
        layers.MaxPooling2D((2,2)),
        layers.Flatten(),
        layers.Dense(32, activation='relu'),
        layers.Dense(10, activation='softmax')
    ])

    model.compile(optimizer=optimizer,
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    return model

# SGD (Gradient Descent)
print("\nUsing SGD (Gradient Descent)")
sgd_model = build_model(tf.keras.optimizers.SGD())
sgd_model.fit(x_train, y_train, epochs=1, verbose=0)
loss_sgd, acc_sgd = sgd_model.evaluate(x_test, y_test, verbose=0)
print("SGD Accuracy:", acc_sgd)

# Adam
print("\nUsing Adam")
adam_model = build_model(tf.keras.optimizers.Adam())
adam_model.fit(x_train, y_train, epochs=1, verbose=0)
loss_adam, acc_adam = adam_model.evaluate(x_test, y_test, verbose=0)
print("Adam Accuracy:", acc_adam)