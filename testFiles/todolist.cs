using System;
using System.Collections.Generic;
using System.IO;

class ToDoListApp
{
    static string filePath = "tasks.txt";
    static List<string> tasks = new List<string>();
    
    static void Main()
    {
        LoadTasks();
        while (true)
        {
            Console.Clear();
            Console.WriteLine("To-Do List Application");
            Console.WriteLine("1. Add Task");
            Console.WriteLine("2. Remove Task");
            Console.WriteLine("3. View Tasks");
            Console.WriteLine("4. Exit");
            Console.Write("Choose an option: ");

            string choice = Console.ReadLine();
            switch (choice)
            {
                case "1": AddTask(); break;
                case "2": RemoveTask(); break;
                case "3": ViewTasks(); break;
                case "4": SaveTasks(); return;
                default: Console.WriteLine("Invalid option. Press Enter to try again."); Console.ReadLine(); break;
            }
        }
    }

    static void AddTask()
    {
        Console.Write("Enter new task: ");
        string task = Console.ReadLine();
        if (!string.IsNullOrWhiteSpace(task))
        {
            tasks.Add(task);
            Console.WriteLine("Task added successfully!");
        }
        else
        {
            Console.WriteLine("Task cannot be empty!");
        }
        Console.ReadLine();
    }

    static void RemoveTask()
    {
        ViewTasks();
        Console.Write("Enter task number to remove: ");
        if (int.TryParse(Console.ReadLine(), out int index) && index > 0 && index <= tasks.Count)
        {
            tasks.RemoveAt(index - 1);
            Console.WriteLine("Task removed successfully!");
        }
        else
        {
            Console.WriteLine("Invalid task number!");
        }
        Console.ReadLine();
    }

    static void ViewTasks()
    {
        Console.WriteLine("\nYour Tasks:");
        if (tasks.Count == 0)
        {
            Console.WriteLine("No tasks available.");
        }
        else
        {
            for (int i = 0; i < tasks.Count; i++)
            {
                Console.WriteLine($"{i + 1}. {tasks[i]}");
            }
        }
        Console.WriteLine("\nPress Enter to continue...");
        Console.ReadLine();
    }

    static void SaveTasks()
    {
        File.WriteAllLines(filePath, tasks);
        Console.WriteLine("Tasks saved successfully!");
    }

    static void LoadTasks()
    {
        if (File.Exists(filePath))
        {
            tasks = new List<string>(File.ReadAllLines(filePath));
        }
    }
}
