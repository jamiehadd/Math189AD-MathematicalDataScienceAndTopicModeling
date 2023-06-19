# MATH 189: Mathematical Data Science & Topic Modeling

Prof. Jamie Haddock, <jhaddock@g.hmc.edu>

In this course, students will learn about common mathematical representations of data, the mathematical foundations of matrix factorization and tensor decomposition, and their application to many tasks in machine learning and data science.  These decomposition techniques are integral tools in studying large-scale and multi-modal data and form the basis for many approaches to the topic modeling, dimension reduction, and clustering tasks.  Potential topics include PCA, nonnegative matrix factorization, higher-order SVD, nonnegative tensor decompositions, K-means clustering, optimization techniques for these models, and applications in machine learning, data science, signal processing, and network science.


## AIMS FOR THE COURSE

In this course, we will engage with current mathematical and data scientific research.  It has been designed to strengthen your skills in reading and analyzing research papers, and writing and presenting your own research.


## READING ASSIGNMENTS

Reading assignments are the primary way that you will engage with course content outside of lecture.  These readings serve several important purposes, including to introduce you to state-of-the-art techniques in the field and to develop competency in reading academic papers.

Reading will be assigned weekly and each reading has two components.

The first part is the active reading of the assigned article. You will access the assigned reading via Google Classroom, and then you will engage in active reading of the article via annotations and discussions in Google.

The second part is a short-answer reflection that will be accessed via Gradescope. The overview focuses on big-picture concepts and mathematical ideas from the article and should be completed after you have finished the active reading. You will submit this part directly to Gradescope.

Using Gradescope: If you are registered for this course, you should have already been added to the Gradescope class page. Contact your instructor if you are having problems with access. Gradescope has several tutorial resources, e.g., [Gradescope video tutorials](https://www.gradescope.com/get_started#student-submission).  


## TENTATIVE SCHEDULE

| Week |	Date | Topic |	Assigned Readings | Assignments Due |
| --- | --- | --- | --- | --- |
| 1 |	M | [Syllabus, Class Norms, Ice-breakers](https://docs.google.com/presentation/d/1sZ7tNBJcCzH2ReunDEWXdksORNC-59lKVz3OGpyl064/edit?usp=sharing) | | |	 	 
| | W | [Data and Data Science](https://docs.google.com/presentation/d/1XTkyrbUUcSJppj54eNiQ4f3MpQzPmLlw9n9EMerOlyQ/edit?usp=sharing) | Baker, Matthew. "How to Read a Research Paper." Notices of the American Mathematical Society 67.5 (2020): 660-662. <br> Higham, Nicholas J. "How to Read and Understand a Paper." (2015): 903-906. <br> Optional: Kolda, Tamara. "Mathematics: The Tao of Data Science." Harvard Data Science Review (2020). <br> Optional: Breiman, Leo. "Statistical modeling: The two cultures (with comments and a rejoinder by the author)." Statistical science 16.3 (2001): 199-231.<br> **Due:** W Sep 7 before class ([Reflection 1](https://www.overleaf.com/read/whmmfgptfggs)) | |
| 2	| M |	No Class | | |	 	 
| | W |	[Linear Algebra, Optimization, and Probability Tools](https://docs.google.com/presentation/d/1HO2QVYmiMmgFJ0_6OE1RrSX7ED8y34MtgLVy0PgQNMo/edit?usp=sharing) | Lee, Daniel D., and H. Sebastian Seung. "Learning the parts of objects by non-negative matrix factorization." Nature 401.6755 (1999): 788-791.<br> **Due:** T Sep 13 by end of day ([Reflection 2](https://www.overleaf.com/read/ybgffrdmfhpy))| [Reflection 1](https://www.overleaf.com/read/whmmfgptfggs) |
| 3 | M | [Our lens: Nonnegative Matrix Factorization](https://docs.google.com/presentation/d/1dGcNmc81TWOcC560c3hscwXP1iq-e_DNEGor7Fdye2U/edit?usp=sharing) | | |
| | W | [Discussion](https://docs.google.com/presentation/d/1zxpa5Ozep8amE2qMiLVC3JFWUKhgskp5AoCiFoOgIT8/edit?usp=sharing) and [Tutorial](tutorials/Nonnegative_Matrix_Factorization.ipynb) | Chapter 1 of Gillis, Nicolas. Nonnegative Matrix Factorization. Society for Industrial and Applied Mathematics, 2020. <br> **Due:** T Sep 20 by end of day ([Reflection 3](https://www.overleaf.com/read/fgfjbgvwxckg)) | [Reflection 2](https://www.overleaf.com/read/ybgffrdmfhpy) + [Rubric](https://www.overleaf.com/read/ffzszjstwpqp) (see [rubric guide](files/rubric_details.pdf))|
| 4 | M | [Dimensionality Reduction and Clustering](https://docs.google.com/presentation/d/1MXszby71RCv7iDu-aJNbuH0-Tj6OqFkUrbl0RUxaWqw/edit?usp=sharing) | | |	 
| | W | [Discussion](https://docs.google.com/presentation/d/1X36kEOgeSQgpj8nBYcDzXGbyISqCeyUYOGazGBwDm4M/edit?usp=sharing) and [Tutorial](tutorials/NMF_for_Dimensionality_Reduction_and_Clustering.ipynb)| Kolda, Tamara G., and Brett W. Bader. "Tensor decompositions and applications." SIAM review 51.3 (2009): 455-500. <br> Rabanser, Stephan, Oleksandr Shchur, and Stephan Günnemann. "Introduction to tensor decompositions and their applications in machine learning." arXiv preprint arXiv:1711.10781 (2017). <br> **Due:** T Sep 27 by end of day ([Reflection 4](https://www.overleaf.com/read/vdkxfnrmvvsy)) | [Reflection 3](https://www.overleaf.com/read/fgfjbgvwxckg) |
| 5 | M | [Tensor Decomposition Models](https://docs.google.com/presentation/d/1IF2vuhrUDkmqqed06AQHjvjDzT17raxGU_Njc1HcmjM/edit?usp=sharing) | | |
| | W | [Discussion](https://docs.google.com/presentation/d/1vO7p_Ne3VgquMFck46SS1P39bC1SyCA6LVt7gsJXny8/edit?usp=sharing) and [Tutorial](tutorials/Tensor_Decomposition_Models.ipynb) | Lee, D. D., and H. S. Seung. "Algorithms for Non-Negative Matrix Factorization. NIPS (2000)." Google Scholar: 556-562. <br> **Due:** T Oct 4 by end of day ([Reflection 5](https://www.overleaf.com/read/xxjyzjpmxhbc)) | [Reflection 4](https://www.overleaf.com/read/vdkxfnrmvvsy) |
| 6 | M | [Training NMF models](https://docs.google.com/presentation/d/10ZC7z4328cAE-ypoMH3kl10a2zKsfYPa9FY3ACXE9pQ/edit?usp=sharing) and [In-class Tutorial](tutorials/In_class_Test_of_Multiplicative_Updates.ipynb)	| | |  	 
| | W | [Discussion](https://docs.google.com/presentation/d/1uyddpu4VsYSfSagh_o-w30VZd79LiUXrK9uYzwvM7Bs/edit?usp=sharing) and [Tutorial](tutorials/Multiplicative_Updates_for_NMF.ipynb) | |	[Reflection 5](https://www.overleaf.com/read/xxjyzjpmxhbc) |
| 7 | M | [Overview of NMF Variants](https://docs.google.com/presentation/d/1r3vpG7ZVmE1TF5vshJ9cleAEfYJ862TnZBJ06RWkJrM/edit?usp=sharing) | | | 	 
| | W | [Team Building](https://docs.google.com/presentation/d/1BlrZrwXv4SID_BE00W61rB4cPVj7GyHhexjBF07icHM/edit?usp=sharing) | |	[Topic brainstorm](https://www.overleaf.com/read/sgbfrvqsyvnv) |
| 8 | M | No Class | | |	 	 
| | W | [Statistical Foundations of NMF](https://docs.google.com/presentation/d/1GL-soQ-_gYravYLqrTM89e3bKdL5Dhd9qrCJu0wqJaA/edit?usp=sharing) | | |
| 9 | M | Group pitch development | | |
| | W | [Topic pitches, Writing Center Visit, and Mid-Semester Evaluations](https://docs.google.com/presentation/d/1CtMzzWwHsId7r7aMeGFkOjlHni-2fbgBhctiSYEkWio/edit?usp=sharing) | Lee, Hyekyoung, Jiho Yoo, and Seungjin Choi. "Semi-supervised nonnegative matrix factorization." IEEE Signal Processing Letters 17.1 (2009): 4-7. <br> Haddock, Jamie, et al. "Semi-supervised NMF Models for Topic Modeling in Learning Tasks." arXiv preprint arXiv:2010.07956 (2020). <br> **Due:** T Nov 1 by end of day ([Reflection 6](https://www.overleaf.com/read/xskfwfknbmpp)) | [Group pitch](https://www.overleaf.com/read/sgbfrvqsyvnv) |
| | F | | | [Group abstract](https://www.overleaf.com/read/sgbfrvqsyvnv) |
| 10 | M | [Supervised NMF Variants](https://docs.google.com/presentation/d/1KKKNOaZ0Q3jv5uvQDejbSTuoMxoP_expCx-2O4fXacI/edit?usp=sharing) | | | 	 
| | W | [Discussion](https://docs.google.com/presentation/d/1wc1bbVPoFs0Rqfxt_kP8mjyVpI9d5LR254bW4-VC_wY/edit?usp=sharing) and [Tutorial](tutorials/Guided_NMF_Demo_Twitter.ipynb) | Kuang, Da, Sangwoon Yun, and Haesun Park. "SymNMF: nonnegative low-rank approximation of a similarity matrix for graph clustering." Journal of Global Optimization 62.3 (2015): 545-574. <br> **Due:**  T Nov 8 by end of day ([Reflection 7](https://www.overleaf.com/read/fqhgggvxkvdv)) | [Reflection 6](https://www.overleaf.com/read/xskfwfknbmpp) |
| 11 | M | [Community Detection with NMF](https://docs.google.com/presentation/d/1Kg6f7Ia79XGb44NPt6xAfv1dUS6vbcM8edi5T-g7zLs/edit?usp=sharing) and [In-class Tutorial](tutorials/In_class_Test_of_SymNMF_Multiplicative_Updates.ipynb) | |	[Midsemester reflection](https://www.overleaf.com/read/dwkhpgtxnvqz) |
| | W | [Discussion](https://docs.google.com/presentation/d/1DLlRwbqhD6Bauf9PvtwppN941iJLz4ztOWwTHG1JnFM/edit?usp=sharing) and [Tutorial](tutorials/Community_Detection_with_SymNMF.ipynb) | De Handschutter, Pierre, Nicolas Gillis, and Xavier Siebert. "Deep matrix factorizations." arXiv preprint arXiv:2010.00380 (2020).<br> **Due:** T Nov 15 by end of day ([Reflection 8](https://www.overleaf.com/read/gygbqcfywwxd)) | [Reflection 7](https://www.overleaf.com/read/fqhgggvxkvdv) |
| 12 | M | [Hierarchical NMF](https://docs.google.com/presentation/d/1YZXjTrkg3BmJwQiJJpy75OUd3P8SEwbNoXnMz7quQmE/edit?usp=sharing) | | |
| | W | [Discussion](https://docs.google.com/presentation/d/1NWfuLzjDrLlGskxX4p-yfFZ_c1JTEH5wmVO5lynRB6M/edit?usp=sharing) | Koren, Yehuda, Robert Bell, and Chris Volinsky. "Matrix factorization techniques for recommender systems." Computer 42.8 (2009): 30-37.<br> **Due:** T Nov 22 by end of day ([Reflection 9](https://www.overleaf.com/read/ncjyrtjmtzff)) | [Reflection 8](https://www.overleaf.com/read/gygbqcfywwxd) |
| 13 | M | [NMF Applications: Recommender Systems and more](https://docs.google.com/presentation/d/18cW1elrID10_f2WefZAu7VxHQQd5ORo7JIlhjBp5M3Y/edit?usp=sharing) | | [Reflection 9](https://www.overleaf.com/read/ncjyrtjmtzff) |
| | W | No Class | | |  	 
| 14 | M | [Convex NMF and Archetypal Analysis](https://docs.google.com/presentation/d/1bmEFv0Nz8Hxp0CndUm3Youo6kZoScCo8x0C-7kE1mek/edit?usp=sharing) | | |	 	 
| | W | No Class | | |
| 15 | M | Group Project Presentations | | [Group extended summary](https://www.overleaf.com/read/sgbfrvqsyvnv) |
| | W | Group Project Presentations | | |	 
| Finals | W | | | [Group paper](https://www.overleaf.com/read/sgbfrvqsyvnv) |
| | F | | | [Final reflection](https://www.overleaf.com/read/npbktkfrzybw) |


## FINAL PROJECT
Our final project will be a group project (consisting of 3-4 students per team) focused on a topic of the team's choosing.  The project components will be the required parts of a mock (or perhaps real!) submission to the nice annual IEEE conference ["Asilomar Conference on Signals, Systems, and Computers"](https://www.asilomarsscconf.org/).  These are a 100–200 word abstract, an extended summary (500–1000 words plus figures), a technical presentation, and a full paper (5-8 pages).  Like the conference, you will submit the abstract and extended summary in advance of your group final presentation, and the final paper after your presentation.   

Details here: [Final project](https://www.overleaf.com/read/sgbfrvqsyvnv)
