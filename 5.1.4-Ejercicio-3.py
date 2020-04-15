class ExerciseSession :
    def __init__(self,exercise_name="none",intensity="none",duration =0):
        self.exercise_name =exercise_name
        self.intensity = intensity
        self.duration = duration
        
    def get_exercise(self):
        return self.exercise_name

    def get_intensity(self):
        return self.intensity

    def get_duration(self):
        return self.duration
    def set_exercise (self,exercise_name) :
        self.exercise_name =exercise_name

    def set_duration (self,duration) :
        self.duration = duration
        
    def set_intensity (self,intensity) :
        self.intensity = intensity
    
    def calories_burned(self):
        calories = ""
        if self.intensity == "Low" :
            calories= 4 * self.duration
        elif self.intensity == "Moderate" :
            calories = 8 * self.duration
        elif self.intensity == "High" :
            calories = 12 * self.duration
        return calories    
    
        
         
new_exercise = ExerciseSession("Running", "Low", 60)
print(new_exercise.calories_burned())
new_exercise.set_exercise("Swimming")
new_exercise.set_intensity("High")
new_exercise.set_duration(30)
print(new_exercise.calories_burned())
