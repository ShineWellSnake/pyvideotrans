# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cn.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1488, 771)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setToolTip("")
        self.splitter.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.splitter.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.splitter.setLineWidth(2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 3, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.layout_source_mp4 = QtWidgets.QFormLayout()
        self.layout_source_mp4.setObjectName("layout_source_mp4")
        self.btn_get_video = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_get_video.sizePolicy().hasHeightForWidth())
        self.btn_get_video.setSizePolicy(sizePolicy)
        self.btn_get_video.setMinimumSize(QtCore.QSize(120, 35))
        self.btn_get_video.setStyleSheet("")
        self.btn_get_video.setObjectName("btn_get_video")
        self.layout_source_mp4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.btn_get_video)
        self.source_mp4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.source_mp4.setMinimumSize(QtCore.QSize(0, 35))
        self.source_mp4.setInputMask("")
        self.source_mp4.setText("")
        self.source_mp4.setReadOnly(True)
        self.source_mp4.setObjectName("source_mp4")
        self.layout_source_mp4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.source_mp4)
        self.horizontalLayout_6.addLayout(self.layout_source_mp4)
        self.layout_target_dir = QtWidgets.QFormLayout()
        self.layout_target_dir.setObjectName("layout_target_dir")
        self.btn_save_dir = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_save_dir.setMinimumSize(QtCore.QSize(120, 35))
        self.btn_save_dir.setStyleSheet("")
        self.btn_save_dir.setObjectName("btn_save_dir")
        self.layout_target_dir.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.btn_save_dir)
        self.target_dir = QtWidgets.QLineEdit(self.layoutWidget)
        self.target_dir.setMinimumSize(QtCore.QSize(0, 35))
        self.target_dir.setInputMask("")
        self.target_dir.setText("")
        self.target_dir.setReadOnly(True)
        self.target_dir.setObjectName("target_dir")
        self.layout_target_dir.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.target_dir)
        self.horizontalLayout_6.addLayout(self.layout_target_dir)
        self.open_targetdir = QtWidgets.QPushButton(self.layoutWidget)
        self.open_targetdir.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_targetdir.sizePolicy().hasHeightForWidth())
        self.open_targetdir.setSizePolicy(sizePolicy)
        self.open_targetdir.setMinimumSize(QtCore.QSize(50, 30))
        self.open_targetdir.setObjectName("open_targetdir")
        self.horizontalLayout_6.addWidget(self.open_targetdir)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.layout_translate_type = QtWidgets.QFormLayout()
        self.layout_translate_type.setObjectName("layout_translate_type")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(0, 35))
        self.label_9.setObjectName("label_9")
        self.layout_translate_type.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.translate_type = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.translate_type.sizePolicy().hasHeightForWidth())
        self.translate_type.setSizePolicy(sizePolicy)
        self.translate_type.setMinimumSize(QtCore.QSize(0, 35))
        self.translate_type.setObjectName("translate_type")
        self.layout_translate_type.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.translate_type)
        self.horizontalLayout_5.addLayout(self.layout_translate_type)
        self.layout_proxy = QtWidgets.QFormLayout()
        self.layout_proxy.setObjectName("layout_proxy")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 35))
        self.label.setObjectName("label")
        self.layout_proxy.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.proxy = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proxy.sizePolicy().hasHeightForWidth())
        self.proxy.setSizePolicy(sizePolicy)
        self.proxy.setMinimumSize(QtCore.QSize(0, 35))
        self.proxy.setObjectName("proxy")
        self.layout_proxy.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.proxy)
        self.horizontalLayout_5.addLayout(self.layout_proxy)
        self.listen_layout = QtWidgets.QVBoxLayout()
        self.listen_layout.setObjectName("listen_layout")
        self.listen_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.listen_btn.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listen_btn.sizePolicy().hasHeightForWidth())
        self.listen_btn.setSizePolicy(sizePolicy)
        self.listen_btn.setObjectName("listen_btn")
        self.listen_layout.addWidget(self.listen_btn)
        self.horizontalLayout_5.addLayout(self.listen_layout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.layout_source_language = QtWidgets.QFormLayout()
        self.layout_source_language.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.layout_source_language.setObjectName("layout_source_language")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 35))
        self.label_2.setObjectName("label_2")
        self.layout_source_language.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.source_language = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.source_language.sizePolicy().hasHeightForWidth())
        self.source_language.setSizePolicy(sizePolicy)
        self.source_language.setMinimumSize(QtCore.QSize(0, 35))
        self.source_language.setObjectName("source_language")
        self.layout_source_language.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.source_language)
        self.horizontalLayout.addLayout(self.layout_source_language)
        self.layout_target_language = QtWidgets.QFormLayout()
        self.layout_target_language.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.layout_target_language.setObjectName("layout_target_language")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 35))
        self.label_3.setObjectName("label_3")
        self.layout_target_language.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.target_language = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.target_language.sizePolicy().hasHeightForWidth())
        self.target_language.setSizePolicy(sizePolicy)
        self.target_language.setMinimumSize(QtCore.QSize(0, 35))
        self.target_language.setObjectName("target_language")
        self.layout_target_language.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.target_language)
        self.horizontalLayout.addLayout(self.layout_target_language)
        self.layout_tts_type = QtWidgets.QFormLayout()
        self.layout_tts_type.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.layout_tts_type.setObjectName("layout_tts_type")
        self.tts_text = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tts_text.sizePolicy().hasHeightForWidth())
        self.tts_text.setSizePolicy(sizePolicy)
        self.tts_text.setMinimumSize(QtCore.QSize(0, 35))
        self.tts_text.setObjectName("tts_text")
        self.layout_tts_type.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.tts_text)
        self.tts_type = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tts_type.sizePolicy().hasHeightForWidth())
        self.tts_type.setSizePolicy(sizePolicy)
        self.tts_type.setMinimumSize(QtCore.QSize(0, 35))
        self.tts_type.setObjectName("tts_type")
        self.layout_tts_type.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tts_type)
        self.horizontalLayout.addLayout(self.layout_tts_type)
        self.layout_voice_role = QtWidgets.QFormLayout()
        self.layout_voice_role.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.layout_voice_role.setObjectName("layout_voice_role")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(0, 35))
        self.label_4.setObjectName("label_4")
        self.layout_voice_role.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.voice_role = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.voice_role.sizePolicy().hasHeightForWidth())
        self.voice_role.setSizePolicy(sizePolicy)
        self.voice_role.setMinimumSize(QtCore.QSize(0, 35))
        self.voice_role.setObjectName("voice_role")
        self.layout_voice_role.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.voice_role)
        self.horizontalLayout.addLayout(self.layout_voice_role)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.layout_whisper_model = QtWidgets.QGridLayout()
        self.layout_whisper_model.setObjectName("layout_whisper_model")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(0, 35))
        self.label_5.setObjectName("label_5")
        self.layout_whisper_model.addWidget(self.label_5, 0, 0, 1, 1)
        self.whisper_model = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.whisper_model.sizePolicy().hasHeightForWidth())
        self.whisper_model.setSizePolicy(sizePolicy)
        self.whisper_model.setMinimumSize(QtCore.QSize(0, 35))
        self.whisper_model.setObjectName("whisper_model")
        self.layout_whisper_model.addWidget(self.whisper_model, 0, 1, 1, 1)
        self.whisper_type = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.whisper_type.sizePolicy().hasHeightForWidth())
        self.whisper_type.setSizePolicy(sizePolicy)
        self.whisper_type.setMinimumSize(QtCore.QSize(0, 35))
        self.whisper_type.setObjectName("whisper_type")
        self.layout_whisper_model.addWidget(self.whisper_type, 0, 2, 1, 1)
        self.horizontalLayout_4.addLayout(self.layout_whisper_model)
        self.layout_subtitle_type = QtWidgets.QFormLayout()
        self.layout_subtitle_type.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.layout_subtitle_type.setObjectName("layout_subtitle_type")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(0, 35))
        self.label_8.setObjectName("label_8")
        self.layout_subtitle_type.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.subtitle_type = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subtitle_type.sizePolicy().hasHeightForWidth())
        self.subtitle_type.setSizePolicy(sizePolicy)
        self.subtitle_type.setMinimumSize(QtCore.QSize(0, 35))
        self.subtitle_type.setCurrentText("")
        self.subtitle_type.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.subtitle_type.setObjectName("subtitle_type")
        self.layout_subtitle_type.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.subtitle_type)
        self.horizontalLayout_4.addLayout(self.layout_subtitle_type)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.gaoji_layout_wrap = QtWidgets.QVBoxLayout()
        self.gaoji_layout_wrap.setObjectName("gaoji_layout_wrap")
        self.gaoji_layout_inner = QtWidgets.QHBoxLayout()
        self.gaoji_layout_inner.setObjectName("gaoji_layout_inner")
        self.layout_voice_silence = QtWidgets.QFormLayout()
        self.layout_voice_silence.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.layout_voice_silence.setObjectName("layout_voice_silence")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setMinimumSize(QtCore.QSize(0, 35))
        self.label_7.setObjectName("label_7")
        self.layout_voice_silence.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.voice_silence = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.voice_silence.sizePolicy().hasHeightForWidth())
        self.voice_silence.setSizePolicy(sizePolicy)
        self.voice_silence.setMinimumSize(QtCore.QSize(100, 35))
        self.voice_silence.setObjectName("voice_silence")
        self.layout_voice_silence.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.voice_silence)
        self.gaoji_layout_inner.addLayout(self.layout_voice_silence)
        self.layout_voice_rate = QtWidgets.QFormLayout()
        self.layout_voice_rate.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.layout_voice_rate.setObjectName("layout_voice_rate")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setMinimumSize(QtCore.QSize(0, 35))
        self.label_6.setObjectName("label_6")
        self.layout_voice_rate.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.voice_rate = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.voice_rate.sizePolicy().hasHeightForWidth())
        self.voice_rate.setSizePolicy(sizePolicy)
        self.voice_rate.setMinimumSize(QtCore.QSize(100, 35))
        self.voice_rate.setObjectName("voice_rate")
        self.layout_voice_rate.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.voice_rate)
        self.gaoji_layout_inner.addLayout(self.layout_voice_rate)
        self.voice_autorate = QtWidgets.QCheckBox(self.layoutWidget)
        self.voice_autorate.setMinimumSize(QtCore.QSize(0, 35))
        self.voice_autorate.setObjectName("voice_autorate")
        self.gaoji_layout_inner.addWidget(self.voice_autorate)
        self.video_autorate = QtWidgets.QCheckBox(self.layoutWidget)
        self.video_autorate.setObjectName("video_autorate")
        self.gaoji_layout_inner.addWidget(self.video_autorate)
        self.enable_cuda = QtWidgets.QCheckBox(self.layoutWidget)
        self.enable_cuda.setMinimumSize(QtCore.QSize(0, 35))
        self.enable_cuda.setObjectName("enable_cuda")
        self.gaoji_layout_inner.addWidget(self.enable_cuda)
        self.gaoji_layout_wrap.addLayout(self.gaoji_layout_inner)
        self.verticalLayout_2.addLayout(self.gaoji_layout_wrap)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.show_tips = QtWidgets.QLabel(self.layoutWidget)
        self.show_tips.setText("")
        self.show_tips.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.show_tips.setObjectName("show_tips")
        self.verticalLayout_3.addWidget(self.show_tips)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.startbtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startbtn.sizePolicy().hasHeightForWidth())
        self.startbtn.setSizePolicy(sizePolicy)
        self.startbtn.setMinimumSize(QtCore.QSize(200, 50))
        self.startbtn.setObjectName("startbtn")
        self.horizontalLayout_3.addWidget(self.startbtn)
        self.continue_compos = QtWidgets.QPushButton(self.layoutWidget)
        self.continue_compos.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.continue_compos.sizePolicy().hasHeightForWidth())
        self.continue_compos.setSizePolicy(sizePolicy)
        self.continue_compos.setMinimumSize(QtCore.QSize(260, 35))
        self.continue_compos.setText("")
        self.continue_compos.setObjectName("continue_compos")
        self.horizontalLayout_3.addWidget(self.continue_compos)
        self.stop_djs = QtWidgets.QPushButton(self.layoutWidget)
        self.stop_djs.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stop_djs.sizePolicy().hasHeightForWidth())
        self.stop_djs.setSizePolicy(sizePolicy)
        self.stop_djs.setObjectName("stop_djs")
        self.horizontalLayout_3.addWidget(self.stop_djs)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.process = QtWidgets.QTextBrowser(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.process.sizePolicy().hasHeightForWidth())
        self.process.setSizePolicy(sizePolicy)
        self.process.setMinimumSize(QtCore.QSize(0, 100))
        self.process.setAutoFillBackground(False)
        self.process.setStyleSheet("border:0;\n"
"selection-background-color: rgba(255, 255, 255, 0);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.process.setReadOnly(True)
        self.process.setObjectName("process")
        self.verticalLayout_3.addWidget(self.process)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.subtitle_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.subtitle_layout.setContentsMargins(3, 0, 0, 0)
        self.subtitle_layout.setObjectName("subtitle_layout")
        self.layout_sub_bottom = QtWidgets.QHBoxLayout()
        self.layout_sub_bottom.setObjectName("layout_sub_bottom")
        self.subtitle_layout.addLayout(self.layout_sub_bottom)
        self.horizontalLayout_7.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1488, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu_Key = QtWidgets.QMenu(self.menuBar)
        self.menu_Key.setObjectName("menu_Key")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_H = QtWidgets.QMenu(self.menuBar)
        self.menu_H.setObjectName("menu_H")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMinimumSize(QtCore.QSize(0, 0))
        self.toolBar.setMovable(True)
        self.toolBar.setIconSize(QtCore.QSize(100, 40))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.actionbaidu_key = QtWidgets.QAction(MainWindow)
        self.actionbaidu_key.setObjectName("actionbaidu_key")
        self.actionchatgpt_key = QtWidgets.QAction(MainWindow)
        self.actionchatgpt_key.setObjectName("actionchatgpt_key")
        self.actiondeepL_key = QtWidgets.QAction(MainWindow)
        self.actiondeepL_key.setObjectName("actiondeepL_key")
        self.action_tool = QtWidgets.QAction(MainWindow)
        self.action_tool.setObjectName("action_tool")
        self.action_vlc = QtWidgets.QAction(MainWindow)
        self.action_vlc.setObjectName("action_vlc")
        self.action_ffmpeg = QtWidgets.QAction(MainWindow)
        self.action_ffmpeg.setObjectName("action_ffmpeg")
        self.action_git = QtWidgets.QAction(MainWindow)
        self.action_git.setObjectName("action_git")
        self.action_issue = QtWidgets.QAction(MainWindow)
        self.action_issue.setObjectName("action_issue")
        self.action_clone = QtWidgets.QAction(MainWindow)
        self.action_clone.setObjectName("action_clone")
        self.actiondeepLX_address = QtWidgets.QAction(MainWindow)
        self.actiondeepLX_address.setObjectName("actiondeepLX_address")
        self.action_website = QtWidgets.QAction(MainWindow)
        self.action_website.setObjectName("action_website")
        self.action_discord = QtWidgets.QAction(MainWindow)
        self.action_discord.setObjectName("action_discord")
        self.actiontencent_key = QtWidgets.QAction(MainWindow)
        self.actiontencent_key.setObjectName("actiontencent_key")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.action_biaozhun = QtWidgets.QAction(MainWindow)
        self.action_biaozhun.setCheckable(True)
        self.action_biaozhun.setChecked(True)
        self.action_biaozhun.setObjectName("action_biaozhun")
        self.action_tiquzimu_no = QtWidgets.QAction(MainWindow)
        self.action_tiquzimu_no.setCheckable(True)
        self.action_tiquzimu_no.setObjectName("action_tiquzimu_no")
        self.action_zimu_video = QtWidgets.QAction(MainWindow)
        self.action_zimu_video.setCheckable(True)
        self.action_zimu_video.setObjectName("action_zimu_video")
        self.action_zimu_peiyin = QtWidgets.QAction(MainWindow)
        self.action_zimu_peiyin.setCheckable(True)
        self.action_zimu_peiyin.setObjectName("action_zimu_peiyin")
        self.action_yuyinshibie = QtWidgets.QAction(MainWindow)
        self.action_yuyinshibie.setObjectName("action_yuyinshibie")
        self.action_yuyinhecheng = QtWidgets.QAction(MainWindow)
        self.action_yuyinhecheng.setObjectName("action_yuyinhecheng")
        self.action_tiquzimu = QtWidgets.QAction(MainWindow)
        self.action_tiquzimu.setCheckable(True)
        self.action_tiquzimu.setObjectName("action_tiquzimu")
        self.action_yinshipinfenli = QtWidgets.QAction(MainWindow)
        self.action_yinshipinfenli.setObjectName("action_yinshipinfenli")
        self.action_yingyinhebing = QtWidgets.QAction(MainWindow)
        self.action_yingyinhebing.setObjectName("action_yingyinhebing")
        self.action_geshi = QtWidgets.QAction(MainWindow)
        self.action_geshi.setObjectName("action_geshi")
        self.action_hun = QtWidgets.QAction(MainWindow)
        self.action_hun.setObjectName("action_hun")
        self.action_fanyi = QtWidgets.QAction(MainWindow)
        self.action_fanyi.setObjectName("action_fanyi")
        self.actionazure_key = QtWidgets.QAction(MainWindow)
        self.actionazure_key.setObjectName("actionazure_key")
        self.menu_Key.addAction(self.actionbaidu_key)
        self.menu_Key.addSeparator()
        self.menu_Key.addAction(self.actiontencent_key)
        self.menu_Key.addSeparator()
        self.menu_Key.addAction(self.actionchatgpt_key)
        self.menu_Key.addSeparator()
        self.menu_Key.addAction(self.actionazure_key)
        self.menu_Key.addSeparator()
        self.menu_Key.addAction(self.actiondeepL_key)
        self.menu_Key.addSeparator()
        self.menu_Key.addAction(self.actiondeepLX_address)
        self.menu_Key.addSeparator()
        self.menu.addAction(self.action_tool)
        self.menu.addSeparator()
        self.menu.addAction(self.action_clone)
        self.menu_H.addSeparator()
        self.menu_H.addAction(self.action_website)
        self.menu_H.addSeparator()
        self.menu_H.addAction(self.action_discord)
        self.menu_H.addSeparator()
        self.menu_H.addAction(self.action_git)
        self.menu_H.addSeparator()
        self.menu_H.addAction(self.action_issue)
        self.menu_H.addSeparator()
        self.menu_H.addAction(self.action_vlc)
        self.menu_H.addSeparator()
        self.menu_H.addAction(self.action_ffmpeg)
        self.menu_H.addSeparator()
        self.menu_H.addAction(self.action_about)
        self.menu_H.addSeparator()
        self.menuBar.addAction(self.menu_Key.menuAction())
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_H.menuAction())
        self.toolBar.addAction(self.action_biaozhun)
        self.toolBar.addAction(self.action_tiquzimu)
        self.toolBar.addAction(self.action_tiquzimu_no)
        self.toolBar.addAction(self.action_zimu_video)
        self.toolBar.addAction(self.action_zimu_peiyin)
        self.toolBar.addAction(self.action_yuyinshibie)
        self.toolBar.addAction(self.action_yuyinhecheng)
        self.toolBar.addAction(self.action_yinshipinfenli)
        self.toolBar.addAction(self.action_yingyinhebing)
        self.toolBar.addAction(self.action_geshi)
        self.toolBar.addAction(self.action_hun)
        self.toolBar.addAction(self.action_fanyi)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SP视频翻译配音"))
        self.btn_get_video.setToolTip(_translate("MainWindow", "可选择多个mp4视频，自动排队处理"))
        self.btn_get_video.setText(_translate("MainWindow", "选择视频..."))
        self.source_mp4.setPlaceholderText(_translate("MainWindow", "选择待翻译的mp4视频，可多个，排队处理"))
        self.btn_save_dir.setToolTip(_translate("MainWindow", "选择处理后输出的资源保存到哪里"))
        self.btn_save_dir.setText(_translate("MainWindow", "保存到..."))
        self.target_dir.setPlaceholderText(_translate("MainWindow", "选择翻译后的视频保存到的位置，默认原目录下_video_out中"))
        self.open_targetdir.setToolTip(_translate("MainWindow", "打开保存后的目录"))
        self.open_targetdir.setText(_translate("MainWindow", "打开"))
        self.label_9.setText(_translate("MainWindow", "翻译渠道"))
        self.label.setText(_translate("MainWindow", "代理地址"))
        self.proxy.setPlaceholderText(_translate("MainWindow", "比如 http://127.0.0.1:10809 大陆地区必须填写"))
        self.listen_btn.setToolTip(_translate("MainWindow", "点击试听当前配音角色的发音\n"
"生成配音可能需要数秒，请耐心等待\n"
""))
        self.listen_btn.setText(_translate("MainWindow", "试听配音"))
        self.label_2.setText(_translate("MainWindow", "原始语言"))
        self.source_language.setToolTip(_translate("MainWindow", "原视频发音所用语言"))
        self.label_3.setText(_translate("MainWindow", "目标语言"))
        self.target_language.setToolTip(_translate("MainWindow", "你希望翻译为哪种语言"))
        self.tts_text.setText(_translate("MainWindow", "TTS"))
        self.label_4.setText(_translate("MainWindow", "配音角色"))
        self.voice_role.setToolTip(_translate("MainWindow", "选No代表不进行配音"))
        self.label_5.setText(_translate("MainWindow", "语音模型"))
        self.whisper_model.setToolTip(_translate("MainWindow", "base到large，效果越来越好，但速度也越来越慢"))
        self.whisper_type.setToolTip(_translate("MainWindow", "整体识别适合有无背景音乐，有明显静音的视频。"))
        self.label_8.setText(_translate("MainWindow", "嵌入字幕"))
        self.subtitle_type.setToolTip(_translate("MainWindow", "嵌入式字幕无论哪里播放始终显示字幕，不可隐藏。\n"
"软字幕如果播放器支持，可在播放器中控制显示或隐藏。\n"
"如果你想网页中播放时显示字幕，请选择嵌入式字幕。\n"
""))
        self.label_7.setText(_translate("MainWindow", "静音片段"))
        self.voice_silence.setToolTip(_translate("MainWindow", "默认500ms，越小切分的片段越多"))
        self.voice_silence.setPlaceholderText(_translate("MainWindow", "分割语音的静音时长，单位ms"))
        self.label_6.setText(_translate("MainWindow", "配音语速"))
        self.voice_rate.setToolTip(_translate("MainWindow", "对配音语速整体加速或降速播放"))
        self.voice_rate.setPlaceholderText(_translate("MainWindow", "正数则加速，负数则减速，-90到+90"))
        self.voice_autorate.setToolTip(_translate("MainWindow", "翻译后不同语言下发音时长不同，比如一句话中文3s，翻译为英文可能5s，导致时长和视频不一致。\n"
"2种解决方式:\n"
"1. 强制配音加速播放，以便缩短配音时长和视频对齐\n"
"2. 强制视频慢速播放，以便延长视频时长和配音对齐。\n"
"两者只可选其一"))
        self.voice_autorate.setText(_translate("MainWindow", "配音自动加速?"))
        self.video_autorate.setToolTip(_translate("MainWindow", "翻译后不同语言下发音时长不同，比如一句话中文3s，翻译为英文可能5s，导致时长和视频不一致。\n"
"2种解决方式:\n"
"1. 强制配音加速播放，以便缩短配音时长和视频对齐\n"
"2. 强制视频慢速播放，以便延长视频时长和配音对齐。\n"
"两者只可选其一"))
        self.video_autorate.setText(_translate("MainWindow", "视频自动慢速"))
        self.enable_cuda.setToolTip(_translate("MainWindow", "必须确定有NVIDIA显卡且正确配置了CUDA环境，否则勿选"))
        self.enable_cuda.setText(_translate("MainWindow", "使用CUDA加速"))
        self.startbtn.setText(_translate("MainWindow", "开始"))
        self.stop_djs.setText(_translate("MainWindow", "停止倒计时"))
        self.menu_Key.setTitle(_translate("MainWindow", "设置(&S)"))
        self.menu.setTitle(_translate("MainWindow", "工具(&T)"))
        self.menu_H.setTitle(_translate("MainWindow", "帮助(&H)"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionbaidu_key.setText(_translate("MainWindow", "百度Key"))
        self.actionchatgpt_key.setText(_translate("MainWindow", "ChatGPT Key"))
        self.actiondeepL_key.setText(_translate("MainWindow", "DeepL Key"))
        self.action_tool.setText(_translate("MainWindow", "视频工具箱"))
        self.action_tool.setToolTip(_translate("MainWindow", "一个简单的视频处理工具箱"))
        self.action_vlc.setText(_translate("MainWindow", "VLC解码器"))
        self.action_vlc.setToolTip(_translate("MainWindow", "去VLC官网"))
        self.action_ffmpeg.setText(_translate("MainWindow", "FFmpeg"))
        self.action_ffmpeg.setToolTip(_translate("MainWindow", "去FFmpeg官网"))
        self.action_git.setText(_translate("MainWindow", "github 代码"))
        self.action_issue.setText(_translate("MainWindow", "发个issue"))
        self.action_clone.setText(_translate("MainWindow", "音色克隆"))
        self.actiondeepLX_address.setText(_translate("MainWindow", "DeepLX address"))
        self.action_website.setText(_translate("MainWindow", "文档"))
        self.action_discord.setText(_translate("MainWindow", "Discord"))
        self.actiontencent_key.setText(_translate("MainWindow", "腾讯 Key"))
        self.action_about.setText(_translate("MainWindow", "支持该软件"))
        self.action_biaozhun.setText(_translate("MainWindow", "标准功能模式"))
        self.action_biaozhun.setToolTip(_translate("MainWindow", "显示全部选项，进行视频翻译和配音"))
        self.action_tiquzimu_no.setText(_translate("MainWindow", "视频提取字幕"))
        self.action_tiquzimu_no.setToolTip(_translate("MainWindow", "从本地视频中提取出原始语言的srt字幕"))
        self.action_zimu_video.setText(_translate("MainWindow", "字幕视频合并"))
        self.action_zimu_video.setToolTip(_translate("MainWindow", "将本地已有的srt字幕嵌入视频中"))
        self.action_zimu_peiyin.setText(_translate("MainWindow", "字幕创建配音"))
        self.action_zimu_peiyin.setToolTip(_translate("MainWindow", "本地已有的srt字幕生成配音wav文件"))
        self.action_yuyinshibie.setText(_translate("MainWindow", "语音识别文字"))
        self.action_yuyinshibie.setToolTip(_translate("MainWindow", "将音频或视频中的声音识别后输出srt文字"))
        self.action_yuyinhecheng.setText(_translate("MainWindow", "文字合成语音"))
        self.action_yuyinhecheng.setToolTip(_translate("MainWindow", "将文字或srt字幕文件生成音频wav"))
        self.action_tiquzimu.setText(_translate("MainWindow", "提取字幕翻译"))
        self.action_tiquzimu.setToolTip(_translate("MainWindow", "从本地视频中提取出原始语言的srt字幕,并翻译为目标语言的srt字幕文件"))
        self.action_yinshipinfenli.setText(_translate("MainWindow", "视频音频分离"))
        self.action_yinshipinfenli.setToolTip(_translate("MainWindow", "从视频中分离出音频和无声视频"))
        self.action_yingyinhebing.setText(_translate("MainWindow", "视频字幕合并"))
        self.action_yingyinhebing.setToolTip(_translate("MainWindow", "将音频、视频、字幕合并为一个文件"))
        self.action_geshi.setText(_translate("MainWindow", "文件格式转换"))
        self.action_geshi.setToolTip(_translate("MainWindow", "各种格式互相转换"))
        self.action_hun.setText(_translate("MainWindow", "两个音频混流"))
        self.action_hun.setToolTip(_translate("MainWindow", "将两个音频文件混流为一个音频文件"))
        self.action_fanyi.setText(_translate("MainWindow", "文本字幕翻译"))
        self.action_fanyi.setToolTip(_translate("MainWindow", "将文字或者字幕进行翻译"))
        self.actionazure_key.setText(_translate("MainWindow", "Azure AI"))
