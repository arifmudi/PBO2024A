# Konsep Pewarisan Python dalam Sistem Manajemen Sekolah

## 1. Single Inheritance - Pengelolaan Penilaian

Single inheritance memungkinkan sebuah class turunan mewarisi sifat dan metode dari satu class induk saja, mirip seperti sistem penilaian khusus yang merupakan turunan dari sistem penilaian umum.

### Implementasi Sistem Penilaian
```python
class BaseScoring:
    def __init__(self, student_name, subject):
        self.student_name = student_name
        self.subject = subject
        self.scores = []
    
    def add_score(self, score):
        if 0 <= score <= 100:
            self.scores.append(score)
        else:
            raise ValueError("Nilai harus antara 0-100")
    
    def get_average(self):
        return sum(self.scores) / len(self.scores) if self.scores else 0

class PracticalScoring(BaseScoring):
    def __init__(self, student_name, subject, lab_name):
        super().__init__(student_name, subject)
        self.lab_name = lab_name
        self.attendance = []
    
    def add_attendance(self, date, status):
        self.attendance.append({"date": date, "status": status})
    
    def calculate_final_score(self):
        attendance_score = len([a for a in self.attendance if a["status"] == "present"]) / len(self.attendance) * 30
        practice_score = self.get_average() * 0.7
        return attendance_score + practice_score

# Penggunaan
physics_lab = PracticalScoring("Alex", "Fisika", "Lab Fisika 1")
physics_lab.add_score(85)
physics_lab.add_score(90)
physics_lab.add_attendance("2024-01-01", "present")
physics_lab.add_attendance("2024-01-08", "present")
print(f"Nilai Akhir: {physics_lab.calculate_final_score()}")
```

### Kapan Menggunakan
- Saat membuat variasi penilaian khusus
- Ketika ada sistem yang merupakan spesialisasi dari sistem lain
- Saat ingin memperluas fungsi dasar tanpa mengubah sistem utama

## 2. Super() dalam Sistem Presensi

### Konsep dan Manfaat Super()
Super() memungkinkan:
- Pemanggilan konstruktor class induk
- Penggunaan method dari class induk
- Perluasan fungsi tanpa duplikasi
- Pengelolaan hierarki class yang bersih

### Implementasi Sistem Presensi
```python
class Attendance:
    def __init__(self, location, max_capacity):
        self.location = location
        self.max_capacity = max_capacity
        self.attendees = []
    
    def add_attendee(self, person):
        if len(self.attendees) < self.max_capacity:
            self.attendees.append(person)
            return True
        return False

class ClassAttendance(Attendance):
    def __init__(self, location, max_capacity, subject, teacher):
        super().__init__(location, max_capacity)
        self.subject = subject
        self.teacher = teacher
        self.late_students = []
    
    def add_late_student(self, student, minutes_late):
        super().add_attendee(student)
        self.late_students.append({
            "student": student,
            "minutes_late": minutes_late
        })
        return f"Siswa {student} terlambat {minutes_late} menit"

# Penggunaan
math_class = ClassAttendance("Ruang 301", 30, "Matematika", "Mrs. Smith")
math_class.add_attendee("John")
print(math_class.add_late_student("Sarah", 15))
```

## 3. Jenis Inheritance dalam Konteks Sekolah

### Tabel Perbandingan Sistem Akademik

| Jenis | Contoh Sistem Sekolah | Implementasi | Kegunaan | Tingkat Kompleksitas |
|-------|----------------------|--------------|-----------|---------------------|
| Single | Ujian → UjianOnline | Satu turunan | Spesialisasi penilaian | Rendah |
| Multiple | NilaiAkademik + NilaiEkskul → NilaiAkhir | Gabungan nilai | Penilaian komprehensif | Tinggi |
| Multilevel | Siswa → SiswaKelas → SiswaLulus | Proses bertahap | Tracking progress siswa | Sedang |
| Hierarchical | Pegawai → [Guru, Staff, Kepala] | Struktur organisasi | Manajemen SDM | Sedang |
| Hybrid | Kombinasi sistem di atas | Sistem kompleks | Manajemen sekolah lengkap | Sangat Tinggi |

### Implementasi Multiple Inheritance - Sistem Penilaian Komprehensif
```python
class AcademicScore:
    def calculate_academic(self, scores):
        return sum(scores) / len(scores)

class ExtracurricularScore:
    def calculate_extra(self, activities):
        return sum(act['score'] for act in activities)

class FinalGrade(AcademicScore, ExtracurricularScore):
    def __init__(self, student_name):
        self.student_name = student_name
        self.academic_scores = []
        self.extra_activities = []
    
    def add_academic_score(self, score):
        self.academic_scores.append(score)
    
    def add_activity(self, activity, score):
        self.extra_activities.append({
            'activity': activity,
            'score': score
        })
    
    def calculate_final(self):
        academic = self.calculate_academic(self.academic_scores) * 0.7
        extra = self.calculate_extra(self.extra_activities) * 0.3
        return academic + extra

# Penggunaan
student_grade = FinalGrade("Mike")
student_grade.add_academic_score(85)
student_grade.add_academic_score(90)
student_grade.add_activity("Basketball", 95)
print(f"Nilai Akhir: {student_grade.calculate_final()}")
```

## 4. Override Method dalam Sistem Pelaporan

### Implementasi Report Generator
```python
class BaseReport:
    def __init__(self, title, period):
        self.title = title
        self.period = period
        self.data = []
    
    def add_data(self, item):
        self.data.append(item)
    
    def generate(self):
        return f"Basic Report: {self.title} - {self.period}"

class AcademicReport(BaseReport):
    def __init__(self, title, period, class_name):
        super().__init__(title, period)
        self.class_name = class_name
    
    def generate(self):  # Override
        base = super().generate()
        details = "\n".join([f"- {item}" for item in self.data])
        return f"""
        {base}
        Kelas: {self.class_name}
        Detail Nilai:
        {details}
        """

# Penggunaan
report = AcademicReport("Laporan Semester", "2024-1", "XII IPA 1")
report.add_data("Matematika: 85")
report.add_data("Fisika: 90")
print(report.generate())
```

## 5. Penggunaan Inheritance dalam Sistem Sekolah

Inheritance cocok digunakan untuk:
1. Pengembangan sistem penilaian berbeda
2. Pengelolaan berbagai jenis laporan
3. Manajemen berbagai tipe user
4. Sistem presensi yang bervariasi
5. Pengelolaan kegiatan akademik dan non-akademik

## 6. Komposisi dalam Sistem Sekolah

### Implementasi Sistem Kelas
```python
class Schedule:
    def __init__(self):
        self.schedule = {}
    
    def add_session(self, day, time, subject):
        if day not in self.schedule:
            self.schedule[day] = {}
        self.schedule[day][time] = subject

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
    
    def teach(self):
        return f"{self.name} mengajar {self.subject}"

class Classroom:
    def __init__(self, class_name, homeroom_teacher):
        self.class_name = class_name
        self.homeroom_teacher = homeroom_teacher
        self.schedule = Schedule()  # Komposisi
        self.students = []
        self.subject_teachers = []  # Komposisi
    
    def add_student(self, student):
        self.students.append(student)
    
    def add_subject_teacher(self, teacher):
        self.subject_teachers.append(teacher)
    
    def get_class_info(self):
        return f"""
        Kelas: {self.class_name}
        Wali Kelas: {self.homeroom_teacher}
        Jumlah Siswa: {len(self.students)}
        Jumlah Guru Mata Pelajaran: {len(self.subject_teachers)}
        """

# Penggunaan
math_teacher = Teacher("Mrs. Johnson", "Matematika")
class_xa = Classroom("X-A", "Mr. Brown")
class_xa.add_subject_teacher(math_teacher)
class_xa.schedule.add_session("Senin", "08:00", "Matematika")
print(class_xa.get_class_info())
```

### Menggunakan Komposisi Ketika:
1. Mengelola jadwal kelas yang fleksibel
2. Mengorganisasi struktur kelas
3. Mengelola daftar guru dan siswa
4. Mengatur resources pembelajaran
5. Mengelola kegiatan ekstrakurikuler

Perbedaan utama pendekatan ini:
1. Fokus pada sistem manajemen sekolah
2. Contoh implementasi lebih relevan dengan pendidikan
3. Penggunaan kasus nyata dalam sekolah
4. Struktur data yang sesuai dengan administrasi sekolah
5. Penerapan praktis dalam lingkungan pendidikan
