echo on
cd ..
cd /qspectrumanalyzer

pyuic6 qspectrumanalyzer.ui -o ui_qspectrumanalyzer.py
pyuic6 qspectrumanalyzer_baseline.ui -o ui_qspectrumanalyzer_baseline.py
pyuic6 qspectrumanalyzer_colors.ui -o ui_qspectrumanalyzer_colors.py
pyuic6 qspectrumanalyzer_persistence.ui -o ui_qspectrumanalyzer_persistence.py
pyuic6 qspectrumanalyzer_settings_help.ui -o ui_qspectrumanalyzer_settings_help.py
pyuic6 qspectrumanalyzer_settings.ui -o ui_qspectrumanalyzer_settings.py
pyuic6 qspectrumanalyzer_smoothing.ui -o ui_qspectrumanalyzer_smoothing.py

pause
