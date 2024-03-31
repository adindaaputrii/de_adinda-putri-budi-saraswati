-- rata-rata kepuasan mentor
SELECT AVG(mentor_satisfaction_score) AS avg_mentor_satisfaction
FROM `project-001-418604.eksplorasi.survey`

-- rata-rata kepuasan cs
SELECT AVG(cs_satisfaction_score) AS avg_cs_satisfaction
FROM `project-001-418604.eksplorasi.survey`

-- rata-rata kepuasan mentor untuk course a
SELECT AVG(mentor_satisfaction_score) AS avg_mentor_satisfaction_course_a
FROM `project-001-418604.eksplorasi.survey`
WHERE course_name = 'Course A';

-- nilai terendah dari kepuasan belajar course c
SELECT MIN(learning_satisfaction_score) AS min_learning_satisfaction_course_c
FROM `project-001-418604.eksplorasi.survey`
WHERE course_name = 'Course C';

-- nilai tertinggi dari kepuasan CS course b
SELECT MAX(cs_satisfaction_score) AS max_cs_satisfaction_course_b
FROM `project-001-418604.eksplorasi.survey`
WHERE course_name = 'Course B';

-- nama course dengan rata-rata kepuasan mentor tertinggi
SELECT course_name, AVG(mentor_satisfaction_score) AS avg_mentor_satisfaction
FROM `project-001-418604.eksplorasi.survey`
GROUP BY course_name
ORDER BY avg_mentor_satisfaction DESC
LIMIT 1;

-- nama course dengan rata-rata kepuasan belajar tertinggi
SELECT course_name, AVG(learning_satisfaction_score) AS avg_learning_satisfaction
FROM `project-001-418604.eksplorasi.survey`
GROUP BY course_name
ORDER BY avg_learning_satisfaction DESC
LIMIT 1;
