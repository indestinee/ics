from ics import current_time
class Config:
    params = [{
        **current_time(),
        'end_date': '20180712', 'end_time': '000000',
        'summary': '机器学习与图像/视频分析', 
        'url': 'http://course.ucas.ac.cn/portal/site/146218/', 
        'description': '''\
    The Report is expected to have decent machine learning content. Even better if it contains applications on image and video processing. For example, it could be a review of recent deep learning research on image recognition, could be a research paper or merely ideas and discussions on how to develop new graphical model or deep learning model on e.g. synthesize realistically looking images. It could also be a scribble of the course material in your own language.

    Report submission: softcopy submitted to the course platform of our university by next Thu (i.e. by July 12) format: single column (NIPS format at https://nips.cc/Conferences/2014/PaperInformation/StyleFiles) 8 pages and above; Each submission should be unique, and no plagiarism is allowed. If in doubt, please clarify with us asap.

    Writing language: Chinese is acceptable while English is preferred (recall this is a course in English)

    The Report is expected to have decent machine learning content. Even better if it contains applications on image and video processing. For example, it could be a review of recent deep learning research on image recognition, could be a research paper or merely ideas and discussions on how to develop new graphical model or deep learning model on e.g. synthesize realistically looking images. It could also be a scribble of the course material in your own language. Report submission: softcopy submitted to the course platform of our university by next Thu (i.e. by July 12) format: single column (NIPS format at https://nips.cc/Conferences/2014/PaperInformation/StyleFiles) 8 pages and above; Each submission should be unique, and no plagiarism is allowed. If in doubt, please clarify with us asap. Writing language: Chinese is acceptable while English is preferred (recall this is a course in English)'''},
    
    ]

cfg = Config()

