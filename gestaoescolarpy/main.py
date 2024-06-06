import tkinter as tk
from tkinter import messagebox
import mysql.connector
from PIL import Image, ImageTk

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="gestao_escolar"
)
cursor = db.cursor()

# Create tables if they don't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(50) UNIQUE,
    senha VARCHAR(50)
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    matricula INT UNIQUE,
    turma VARCHAR(50),
    idade INT
)
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS notas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    aluno_matricula INT,
    disciplina VARCHAR(50),
    nota FLOAT,
    FOREIGN KEY (aluno_matricula) REFERENCES alunos(matricula)
)
""")
db.commit()

# Main Application Class
class SchoolManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestão Escolar")
        self.root.geometry("800x600")
        self.root.configure(bg="blue")
        
        self.show_login_screen()

    def show_login_screen(self):
        self.clear_screen()
        self.logo = ImageTk.PhotoImage(Image.open("logo.png"))
        logo_label = tk.Label(self.root, image=self.logo, bg="blue")
        logo_label.pack(pady=10)

        developers = tk.Label(self.root, text="Desenvolvedores: Danillo Stival, Gabriel Magno, Matheus Barbosa, Wildjames Goiana, Ronald Soares", bg="blue", fg="white", font=("Arial", 12))
        developers.pack(pady=5)

        title = tk.Label(self.root, text="Login", bg="blue", fg="white", font=("Arial", 24))
        title.pack(pady=10)
        
        username_label = tk.Label(self.root, text="Usuário:", bg="blue", fg="white", font=("Arial", 14))
        username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.root, font=("Arial", 14))
        self.username_entry.pack(pady=5)
        
        password_label = tk.Label(self.root, text="Senha:", bg="blue", fg="white", font=("Arial", 14))
        password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.root, show="*", font=("Arial", 14))
        self.password_entry.pack(pady=5)
        
        login_button = tk.Button(self.root, text="Login", bg="white", fg="blue", font=("Arial", 14), command=self.login)
        login_button.pack(pady=20)
        self.change_on_hover(login_button, "blue", "white")
        
        register_button = tk.Button(self.root, text="Registrar", bg="white", fg="blue", font=("Arial", 14), command=self.show_register_screen)
        register_button.pack(pady=5)
        self.change_on_hover(register_button, "blue", "white")
        
    def show_register_screen(self):
        self.clear_screen()

        title = tk.Label(self.root, text="Registrar", bg="blue", fg="white", font=("Arial", 24))
        title.pack(pady=10)
        
        username_label = tk.Label(self.root, text="Usuário:", bg="blue", fg="white", font=("Arial", 14))
        username_label.pack(pady=5)
        self.reg_username_entry = tk.Entry(self.root, font=("Arial", 14))
        self.reg_username_entry.pack(pady=5)
        
        password_label = tk.Label(self.root, text="Senha:", bg="blue", fg="white", font=("Arial", 14))
        password_label.pack(pady=5)
        self.reg_password_entry = tk.Entry(self.root, show="*", font=("Arial", 14))
        self.reg_password_entry.pack(pady=5)
        
        register_button = tk.Button(self.root, text="Registrar", bg="white", fg="blue", font=("Arial", 14), command=self.register)
        register_button.pack(pady=20)
        self.change_on_hover(register_button, "blue", "white")
        
        back_button = tk.Button(self.root, text="Voltar", bg="white", fg="blue", font=("Arial", 14), command=self.show_login_screen)
        back_button.pack(pady=5)
        self.change_on_hover(back_button, "blue", "white")

    def show_main_screen(self):
        self.clear_screen()
        
        self.logo = ImageTk.PhotoImage(Image.open("logo.png"))
        logo_label = tk.Label(self.root, image=self.logo, bg="blue")
        logo_label.pack(pady=10)
        
        developers = tk.Label(self.root, text="Desenvolvedores: Danillo Stival, Gabriel Magno, Matheus Barbosa, Wildjames Goiana, Ronald Soares", bg="blue", fg="white", font=("Arial", 12))
        developers.pack(pady=5)

        title = tk.Label(self.root, text="Selecione uma Opção", bg="blue", fg="white", font=("Arial", 24))
        title.pack(pady=10)
        
        register_student_button = tk.Button(self.root, text="Cadastrar Aluno", bg="white", fg="blue", font=("Arial", 14), command=self.show_register_student_screen)
        register_student_button.pack(pady=10)
        self.change_on_hover(register_student_button, "blue", "white")
        
        add_grade_button = tk.Button(self.root, text="Adicionar Nota", bg="white", fg="blue", font=("Arial", 14), command=self.show_add_grade_screen)
        add_grade_button.pack(pady=10)
        self.change_on_hover(add_grade_button, "blue", "white")

        update_grade_button = tk.Button(self.root, text="Atualizar Nota", bg="white", fg="blue", font=("Arial", 14), command=self.show_update_grade_screen)
        update_grade_button.pack(pady=10)
        self.change_on_hover(update_grade_button, "blue", "white")

        delete_grade_button = tk.Button(self.root, text="Deletar Nota", bg="white", fg="blue", font=("Arial", 14), command=self.show_delete_grade_screen)
        delete_grade_button.pack(pady=10)
        self.change_on_hover(delete_grade_button, "blue", "white")
        
        display_grades_button = tk.Button(self.root, text="Exibir Notas", bg="white", fg="blue", font=("Arial", 14), command=self.show_display_grades_screen)
        display_grades_button.pack(pady=10)
        self.change_on_hover(display_grades_button, "blue", "white")
        
        check_cr_button = tk.Button(self.root, text="Verificar CR", bg="white", fg="blue", font=("Arial", 14), command=self.show_check_cr_screen)
        check_cr_button.pack(pady=10)
        self.change_on_hover(check_cr_button, "blue", "white")
        
        exit_button = tk.Button(self.root, text="Sair do Sistema", bg="white", fg="blue", font=("Arial", 14), command=self.root.quit)
        exit_button.pack(pady=10)
        self.change_on_hover(exit_button, "blue", "white")
        
    def show_register_student_screen(self):
        self.clear_screen()

        title = tk.Label(self.root, text="Cadastrar Aluno", bg="blue", fg="white", font=("Arial", 24))
        title.pack(pady=10)

        name_label = tk.Label(self.root, text="Nome:", bg="blue", fg="white", font=("Arial", 14))
        name_label.pack(pady=5)
        self.name_entry = tk.Entry(self.root, font=("Arial", 14))
        self.name_entry.pack(pady=5)

        matricula_label = tk.Label(self.root, text="Matrícula:", bg="blue", fg="white", font=("Arial", 14))
        matricula_label.pack(pady=5)
        self.matricula_entry = tk.Entry(self.root, font=("Arial", 14))
        self.matricula_entry.pack(pady=5)

        turma_label = tk.Label(self.root, text="Turma:", bg="blue", fg="white", font=("Arial", 14))
        turma_label.pack(pady=5)
        self.turma_entry = tk.Entry(self.root, font=("Arial", 14))
        self.turma_entry.pack(pady=5)

        idade_label = tk.Label(self.root, text="Idade:", bg="blue", fg="white", font=("Arial", 14))
        idade_label.pack(pady=5)
        self.idade_entry = tk.Entry(self.root, font=("Arial", 14))
        self.idade_entry.pack(pady=5)

        register_button = tk.Button(self.root, text="Cadastrar", bg="white", fg="blue", font=("Arial", 14), command=self.register_student)
        register_button.pack(pady=20)
        self.change_on_hover(register_button, "blue", "white")
        
        back_button = tk.Button(self.root, text="Voltar", bg="white", fg="blue", font=("Arial", 14), command=self.show_main_screen)
        back_button.pack(pady=5)
        self.change_on_hover(back_button, "blue", "white")

    def show_add_grade_screen(self):
        self.clear_screen()

        title = tk.Label(self.root, text="Adicionar Nota", bg="blue", fg="white", font=("Arial", 24))
        title.pack(pady=10)

        matricula_label = tk.Label(self.root, text="Matrícula:", bg="blue", fg="white", font=("Arial", 14))
        matricula_label.pack(pady=5)
        self.grade_matricula_entry = tk.Entry(self.root, font=("Arial", 14))
        self.grade_matricula_entry.pack(pady=5)

        subject_label = tk.Label(self.root, text="Disciplina:", bg="blue", fg="white", font=("Arial", 14))
        subject_label.pack(pady=5)
        self.subject_entry = tk.Entry(self.root, font=("Arial", 14))
        self.subject_entry.pack(pady=5)

        grade_label = tk.Label(self.root, text="Nota:", bg="blue", fg="white", font=("Arial", 14))
        grade_label.pack(pady=5)
        self.grade_entry = tk.Entry(self.root, font=("Arial", 14))
        self.grade_entry.pack(pady=5)

        add_button = tk.Button(self.root, text="Adicionar", bg="white", fg="blue", font=("Arial", 14), command=self.add_grade)
        add_button.pack(pady=20)
        self.change_on_hover(add_button, "blue", "white")
        
        back_button = tk.Button(self.root, text="Voltar", bg="white", fg="blue", font=("Arial", 14), command=self.show_main_screen)
        back_button.pack(pady=5)
        self.change_on_hover(back_button, "blue", "white")

    def show_update_grade_screen(self):
        self.clear_screen()

        title = tk.Label(self.root, text="Atualizar Nota", bg="blue", fg="white", font=("Arial", 24))
        title.pack(pady=10)

        matricula_label = tk.Label(self.root, text="Matrícula:", bg="blue", fg="white", font=("Arial", 14))
        matricula_label.pack(pady=5)
        self.update_matricula_entry = tk.Entry(self.root, font=("Arial", 14))
        self.update_matricula_entry.pack(pady=5)

        subject_label = tk.Label(self.root, text="Disciplina:", bg="blue", fg="white", font=("Arial", 14))
        subject_label.pack(pady=5)
        self.update_subject_entry = tk.Entry(self.root, font=("Arial", 14))
        self.update_subject_entry.pack(pady=5)

        new_grade_label = tk.Label(self.root, text="Nova Nota:", bg="blue", fg="white", font=("Arial", 14))
        new_grade_label.pack(pady=5)
        self.new_grade_entry = tk.Entry(self.root, font=("Arial", 14))
        self.new_grade_entry.pack(pady=5)

        update_button = tk.Button(self.root, text="Atualizar", bg="white", fg="blue", font=("Arial", 14), command=self.update_grade)
        update_button.pack(pady=20)
        self.change_on_hover(update_button, "blue", "white")
        
        back_button = tk.Button(self.root, text="Voltar", bg="white", fg="blue", font=("Arial", 14), command=self.show_main_screen)
        back_button.pack(pady=5)
        self.change_on_hover(back_button, "blue", "white")

    def show_delete_grade_screen(self):
        self.clear_screen()

        title = tk.Label(self.root, text="Deletar Nota", bg="blue", fg="white", font=("Arial", 24))
        title.pack(pady=10)

        matricula_label = tk.Label(self.root, text="Matrícula:", bg="blue", fg="white", font=("Arial", 14))
        matricula_label.pack(pady=5)
        self.delete_matricula_entry = tk.Entry(self.root, font=("Arial", 14))
        self.delete_matricula_entry.pack(pady=5)

        subject_label = tk.Label(self.root, text="Disciplina:", bg="blue", fg="white", font=("Arial", 14))
        subject_label.pack(pady=5)
        self.delete_subject_entry = tk.Entry(self.root, font=("Arial", 14))
        self.delete_subject_entry.pack(pady=5)

        delete_button = tk.Button(self.root, text="Deletar", bg="white", fg="blue", font=("Arial", 14), command=self.delete_grade)
        delete_button.pack(pady=20)
        self.change_on_hover(delete_button, "blue", "white")
        
        back_button = tk.Button(self.root, text="Voltar", bg="white", fg="blue", font=("Arial", 14), command=self.show_main_screen)
        back_button.pack(pady=5)
        self.change_on_hover(back_button, "blue", "white")

    def show_display_grades_screen(self):
        self.clear_screen()

        title = tk.Label(self.root, text="Exibir Notas", bg="blue", fg="white", font=("Arial", 24))
        title.pack(pady=10)

        matricula_label = tk.Label(self.root, text="Matrícula:", bg="blue", fg="white", font=("Arial", 14))
        matricula_label.pack(pady=5)
        self.display_matricula_entry = tk.Entry(self.root, font=("Arial", 14))
        self.display_matricula_entry.pack(pady=5)

        display_button = tk.Button(self.root, text="Exibir", bg="white", fg="blue", font=("Arial", 14), command=self.display_grades)
        display_button.pack(pady=20)
        self.change_on_hover(display_button, "blue", "white")
        
        back_button = tk.Button(self.root, text="Voltar", bg="white", fg="blue", font=("Arial", 14), command=self.show_main_screen)
        back_button.pack(pady=5)
        self.change_on_hover(back_button, "blue", "white")

    def show_check_cr_screen(self):
        self.clear_screen()

        title = tk.Label(self.root, text="Verificar CR", bg="blue", fg="white", font=("Arial", 24))
        title.pack(pady=10)

        matricula_label = tk.Label(self.root, text="Matrícula:", bg="blue", fg="white", font=("Arial", 14))
        matricula_label.pack(pady=5)
        self.cr_matricula_entry = tk.Entry(self.root, font=("Arial", 14))
        self.cr_matricula_entry.pack(pady=5)

        check_button = tk.Button(self.root, text="Verificar", bg="white", fg="blue", font=("Arial", 14), command=self.check_cr)
        check_button.pack(pady=20)
        self.change_on_hover(check_button, "blue", "white")
        
        back_button = tk.Button(self.root, text="Voltar", bg="white", fg="blue", font=("Arial", 14), command=self.show_main_screen)
        back_button.pack(pady=5)
        self.change_on_hover(back_button, "blue", "white")

    def register(self):
        username = self.reg_username_entry.get()
        password = self.reg_password_entry.get()

        if not username or not password:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios")
            return

        try:
            cursor.execute("INSERT INTO usuarios (usuario, senha) VALUES (%s, %s)", (username, password))
            db.commit()
            messagebox.showinfo("Sucesso", "Usuário registrado com sucesso")
            self.show_login_screen()
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", "Nome de usuário já existe")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        cursor.execute("SELECT * FROM usuarios WHERE usuario=%s AND senha=%s", (username, password))
        user = cursor.fetchone()

        if user:
            self.show_main_screen()
        else:
            messagebox.showerror("Erro", "Nome de usuário ou senha inválidos")

    def register_student(self):
        name = self.name_entry.get()
        matricula = self.matricula_entry.get()
        turma = self.turma_entry.get()
        idade = self.idade_entry.get()

        if not name or not matricula or not turma or not idade:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios")
            return

        try:
            cursor.execute("INSERT INTO alunos (nome, matricula, turma, idade) VALUES (%s, %s, %s, %s)", (name, matricula, turma, idade))
            db.commit()
            messagebox.showinfo("Sucesso", "Aluno cadastrado com sucesso")
            self.show_main_screen()
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", "Matrícula já existe")

    def add_grade(self):
        matricula = self.grade_matricula_entry.get()
        subject = self.subject_entry.get()
        grade = self.grade_entry.get()

        if not matricula or not subject or not grade:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios")
            return

        try:
            cursor.execute("INSERT INTO notas (aluno_matricula, disciplina, nota) VALUES (%s, %s, %s)", (matricula, subject, grade))
            db.commit()
            messagebox.showinfo("Sucesso", "Nota adicionada com sucesso")
            self.show_main_screen()
        except mysql.connector.Error as err:
            messagebox.showerror("Erro", "Erro ao adicionar nota")

    def update_grade(self):
        matricula = self.update_matricula_entry.get()
        subject = self.update_subject_entry.get()
        new_grade = self.new_grade_entry.get()

        if not matricula or not subject or not new_grade:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios")
            return

        cursor.execute("UPDATE notas SET nota=%s WHERE aluno_matricula=%s AND disciplina=%s", (new_grade, matricula, subject))
        db.commit()

        if cursor.rowcount:
            messagebox.showinfo("Sucesso", "Nota atualizada com sucesso")
        else:
            messagebox.showerror("Erro", "Nenhuma nota encontrada para atualizar")

        self.show_main_screen()

    def delete_grade(self):
        matricula = self.delete_matricula_entry.get()
        subject = self.delete_subject_entry.get()

        if not matricula or not subject:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios")
            return

        cursor.execute("DELETE FROM notas WHERE aluno_matricula=%s AND disciplina=%s", (matricula, subject))
        db.commit()

        if cursor.rowcount:
            messagebox.showinfo("Sucesso", "Nota deletada com sucesso")
        else:
            messagebox.showerror("Erro", "Nenhuma nota encontrada para deletar")

        self.show_main_screen()

    def display_grades(self):
        matricula = self.display_matricula_entry.get()

        if not matricula:
            messagebox.showerror("Erro", "Matrícula é obrigatória")
            return

        cursor.execute("SELECT disciplina, nota FROM notas WHERE aluno_matricula=%s", (matricula,))
        grades = cursor.fetchall()

        if grades:
            grades_text = "\n".join([f"Disciplina: {grade[0]}, Nota: {grade[1]}" for grade in grades])
            messagebox.showinfo("Notas", grades_text)
        else:
            messagebox.showerror("Erro", "Nenhuma nota encontrada para esta matrícula")

    def check_cr(self):
        matricula = self.cr_matricula_entry.get()

        if not matricula:
            messagebox.showerror("Erro", "Matrícula é obrigatória")
            return

        cursor.execute("SELECT AVG(nota) FROM notas WHERE aluno_matricula=%s", (matricula,))
        avg_grade = cursor.fetchone()[0]

        if avg_grade is not None:
            status = "Aprovado" if avg_grade >= 6 else "Reprovado"
            messagebox.showinfo("CR", f"CR: {avg_grade:.2f}\nStatus: {status}")
        else:
            messagebox.showerror("Erro", "Nenhuma nota encontrada para esta matrícula")

    def change_on_hover(self, button, on_hover_color, on_leave_color):
        button.bind("<Enter>", func=lambda e: button.config(background=on_hover_color, foreground=on_leave_color))
        button.bind("<Leave>", func=lambda e: button.config(background=on_leave_color, foreground=on_hover_color))

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Running the Application
if __name__ == "__main__":
    root = tk.Tk()
    app = SchoolManagementApp(root)
    root.mainloop()
