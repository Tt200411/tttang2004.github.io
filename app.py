import matplotlib
matplotlib.use('Agg')  # 使用非交互式后端

import numpy as np
import matplotlib.pyplot as plt
import io
import base64
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许跨域请求

@app.route('/api/generate_oscillator', methods=['POST'])
def generate_oscillator():
    """
    生成振荡器波形图像的API端点
    接收参数：frequency, amplitude, phase
    返回：base64编码的PNG图像
    """
    try:
        # 获取请求参数
        data = request.get_json()
        frequency = float(data.get('frequency', 1.0))
        amplitude = float(data.get('amplitude', 2.0))
        phase = float(data.get('phase', 0.0))
        
        # 参数验证
        if not (0.1 <= frequency <= 10.0):
            return jsonify({'error': '频率必须在0.1-10.0 Hz之间'}), 400
        if not (0.5 <= amplitude <= 5.0):
            return jsonify({'error': '振幅必须在0.5-5.0之间'}), 400
        if not (0.0 <= phase <= 6.28):
            return jsonify({'error': '相位必须在0-2π之间'}), 400
        
        # 生成时间轴数据
        t = np.linspace(0, 4*np.pi, 1000)  # 4π时间范围，1000个采样点
        
        # 计算正弦波
        y = amplitude * np.sin(frequency * t + phase)
        
        # 创建图像
        plt.style.use('seaborn-v0_8')
        fig, ax = plt.subplots(figsize=(12, 6), facecolor='white')
        
        # 绘制波形
        ax.plot(t, y, linewidth=3, color='#667eea', label=f'A={amplitude}, f={frequency}Hz, φ={phase:.2f}rad')
        
        # 设置网格
        ax.grid(True, alpha=0.3)
        ax.axhline(y=0, color='k', linewidth=0.8, alpha=0.3)
        ax.axvline(x=0, color='k', linewidth=0.8, alpha=0.3)
        
        # 设置坐标轴
        ax.set_xlabel('时间 (Time)', fontsize=12)
        ax.set_ylabel('振幅 (Amplitude)', fontsize=12)
        ax.set_title(f'正弦波: y = {amplitude} × sin({frequency}t + {phase:.2f})', fontsize=14, fontweight='bold')
        ax.legend(loc='upper right')
        
        # 设置坐标轴范围
        ax.set_xlim(0, 4*np.pi)
        ax.set_ylim(-amplitude*1.2, amplitude*1.2)
        
        # 设置x轴刻度标签
        pi_ticks = np.array([0, np.pi, 2*np.pi, 3*np.pi, 4*np.pi])
        pi_labels = ['0', 'π', '2π', '3π', '4π']
        ax.set_xticks(pi_ticks)
        ax.set_xticklabels(pi_labels)
        
        plt.tight_layout()
        
        # 将图像转换为base64字符串
        img_buffer = io.BytesIO()
        plt.savefig(img_buffer, format='png', dpi=150, bbox_inches='tight', 
                   facecolor='white', edgecolor='none')
        img_buffer.seek(0)
        img_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
        img_buffer.close()
        
        plt.close(fig)  # 释放内存
        
        return jsonify({
            'success': True,
            'img_base64': img_base64,
            'parameters': {
                'frequency': frequency,
                'amplitude': amplitude,
                'phase': phase
            }
        })
        
    except Exception as e:
        return jsonify({'error': f'生成图像时发生错误: {str(e)}'}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """健康检查端点"""
    return jsonify({'status': 'healthy', 'message': '振荡器API运行正常'})

@app.route('/', methods=['GET'])
def home():
    """首页，提供API使用说明"""
    return jsonify({
        'message': '振荡器API服务',
        'endpoints': {
            '/api/generate_oscillator': 'POST - 生成振荡器波形图像',
            '/api/health': 'GET - 健康检查'
        },
        'example_usage': {
            'url': '/api/generate_oscillator',
            'method': 'POST',
            'body': {
                'frequency': 1.0,
                'amplitude': 2.0,
                'phase': 0.0
            }
        }
    })

if __name__ == '__main__':
    app.run(debug=True)