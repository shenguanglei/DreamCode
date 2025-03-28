
import tensorflow as tf

# 创建一个简单的卷积神经网络模型
model = tf.keras.Sequential([
    tf.keras.layers.InputLayer(input_shape=(224, 224, 3)),  # 输入层
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),   # 卷积层
    tf.keras.layers.MaxPooling2D((2, 2)),                   # 池化层
    tf.keras.layers.Flatten(),                              # 展平层
    tf.keras.layers.Dense(10, activation='softmax')         # 输出层
])

# 编译模型
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# 训练模型（假设已有训练数据）
# train_data 和 train_labels 是您的训练数据
# model.fit(train_data, train_labels, epochs=10, batch_size=32)

# 导出模型为 SavedModel 格式
export_path = "./saved_model"
tf.saved_model.save(
    model,
    export_path,
    signatures={
        "serving_default": model.call.get_concrete_function(
            tf.TensorSpec(shape=[None, 224, 224, 3], dtype=tf.float32)
        )
    }
)

print(f"模型已成功导出到: {export_path}")