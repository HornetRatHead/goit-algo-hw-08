#Tsygankov_HW8_1

import heapq

def min_cost_to_connect_cables(cable_lengths):
    # Ініціалізація пріоритетної черги з усіма кабелями
    heapq.heapify(cable_lengths)
    
    total_cost = 0
    
    while len(cable_lengths) > 1:
        # Вибираємо два найкоротших кабелі з пріоритетної черги
        shortest1 = heapq.heappop(cable_lengths)
        shortest2 = heapq.heappop(cable_lengths)
        
        # Об'єднуємо їх і додаємо витрати до загальної суми
        print(cable_lengths)
        combined_length = shortest1 + shortest2
        print(combined_length)
        total_cost += combined_length
        print(cable_lengths)
        
        # Додаємо об'єднаний кабель назад у пріоритетну чергу
        heapq.heappush(cable_lengths, combined_length)
    
    return total_cost

if __name__ == "__main__":
    # Приклад вхідних даних
    cable_lengths = [7, 8, 4, 9, 6, 12, 12, 4, 9]
    
    # Знаходимо мінімальну суму витрат на об'єднання кабелів
    min_cost = min_cost_to_connect_cables(cable_lengths)
    print("Мінімальні витрати на об'єднання кабелів:", min_cost)