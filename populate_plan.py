# populate_plan.py

from app import db, app
from app import TrainingPlan

with app.app_context():
    # List of plan items
    plan_items = [
        # Week 1
        TrainingPlan(
            week_number=1,
            day='Monday',
            exercise_details="""
**Warm-Up**

- **Dynamic Stretching** (Perform each exercise for 30 seconds to 1 minute):
  1. **Arm Circles**
     - Extend arms out to the sides and make small to large circles forward and backward.
  2. **Shoulder Rolls**
     - Roll shoulders forward and backward in a smooth motion.
  3. **Neck Tilts and Rotations**
     - Gently tilt your head forward, backward, side to side, and rotate in both directions.
  4. **Torso Twists**
     - Stand with feet shoulder-width apart; rotate your upper body left and right.
  5. **Wrist Circles**
     - Extend arms forward and rotate wrists clockwise and counterclockwise.

- **Light Cardio** (Choose one, 5-10 minutes):
  - **Option 1**: Treadmill Walk/Jog
  - **Option 2**: Elliptical Machine
  - **Option 3**: Stationary Bike
  - **Option 4**: Stair Climber

- **Mobility Drills** (Perform 1-2 sets of 10 reps each):
  1. **Scapular Push-Ups**
     - In a push-up position with arms straight, squeeze shoulder blades together and then push them apart without bending the elbows.
  2. **Band Pull-Aparts**
     - Hold a resistance band at chest level with arms extended; pull the band apart by squeezing shoulder blades together.
  3. **Wall Slides**
     - Stand with your back against a wall, elbows at 90 degrees; slide arms up and down while keeping them in contact with the wall.

**Strength Training**

1. **Bench Press**
   - 5 sets x 5 reps
2. **Pull-Ups or Lat Pull-Downs**
   - 4 sets x 8 reps
3. **Overhead Press**
   - 4 sets x 6 reps
4. **Bent-Over Rows**
   - 4 sets x 8 reps
5. **Push-Ups**
   - 3 sets x max reps

**Core Work**

- **Plank Holds**
  - 3 sets x 1 minute
- **Hanging Leg Raises**
  - 3 sets x 12 reps

**Cool-Down**

- **Static Stretching**: Chest, Shoulders, Triceps
- **Foam Rolling**: Upper Back, Lats
"""
        ),
        TrainingPlan(
            week_number=1,
            day='Tuesday',
            exercise_details="""
**Strict Cardio**

Choose one of the following cardio workouts:

1. **Steady-State Cardio** (45-60 minutes):
   - **Option 1**: Outdoor Run or Treadmill
     - Moderate pace (60-70% of maximum heart rate)
   - **Option 2**: Cycling (Stationary Bike or Outdoor)
   - **Option 3**: Elliptical Trainer
   - **Option 4**: Stair Climber (30-45 minutes)

2. **Interval Training**:
   - **Warm-Up**: 10 minutes of light cardio
   - **Workout**:
     - **Option 1**: High-Intensity Interval Training (HIIT) on Treadmill
       - 1-minute sprint at high intensity
       - 2 minutes of walking or light jogging
       - Repeat for 20-30 minutes
     - **Option 2**: Stair Climber Intervals
       - 2 minutes at high intensity
       - 2 minutes at low intensity
       - Repeat for 20-30 minutes
     - **Option 3**: Elliptical Intervals
       - 1 minute of fast pace with high resistance
       - 2 minutes of moderate pace with low resistance
       - Repeat for 20-30 minutes
   - **Cool-Down**: 5-10 minutes of light cardio and stretching

**Additional Notes**

- **Hydration**: Stay well-hydrated before, during, and after the session.
- **Heart Rate Monitoring**: Aim for 70-85% of your maximum heart rate during high-intensity intervals.
"""
        ),
        TrainingPlan(
            week_number=1,
            day='Wednesday',
            exercise_details="""
**Warm-Up**

- **Dynamic Stretching** (Perform each exercise for 30 seconds to 1 minute):
  1. **Leg Swings**
     - Swing each leg forward and backward, then side to side.
  2. **Hip Circles**
     - Place hands on hips; make circles with your hips clockwise and counterclockwise.
  3. **Ankle Rotations**
     - Rotate each ankle clockwise and counterclockwise.
  4. **High Knees**
     - March in place, bringing knees up towards your chest.
  5. **Butt Kicks**
     - Jog in place, bringing heels up to touch the glutes.

- **Light Cardio** (Choose one, 5-10 minutes):
  - **Option 1**: Treadmill Walk/Light Jog
  - **Option 2**: Stair Climber
  - **Option 3**: Elliptical Machine
  - **Option 4**: Stationary Bike

- **Mobility Drills** (Perform 1-2 sets of 10 reps each):
  1. **Glute Bridges**
  2. **Bodyweight Squats**
  3. **Lunge with Twist**

**Strength Training**

1. **Back Squats**
   - 5 sets x 5 reps
2. **Deadlifts**
   - 5 sets x 5 reps
3. **Walking Lunges**
   - 3 sets x 10 reps per leg
4. **Box Jumps**
   - 3 sets x 8 reps
5. **Calf Raises**
   - 3 sets x 15 reps

**Core Work**

- **Russian Twists**
  - 3 sets x 20 reps
- **Supermans**
  - 3 sets x 12 reps

**Cool-Down**

- **Static Stretching**: Hamstrings, Quads, Glutes
- **Foam Rolling**: Calves, IT Bands, Hamstrings
"""
        ),
        TrainingPlan(
            week_number=1,
            day='Thursday',
            exercise_details="""
**Strict Cardio**

Choose a different option from Tuesday to keep the workouts varied:

1. **Long-Distance Cardio**:
   - **Option 1**: Outdoor Run or Treadmill
     - Distance: 5-7 miles
   - **Option 2**: Cycling
     - Distance: 15-20 miles
   - **Option 3**: Swimming
     - Distance: 1,500-2,000 meters

2. **Cross-Training Circuit**:
   - **Warm-Up**: 5 minutes of light cardio
   - **Circuit Exercises** (perform each for 1 minute, rest 30 seconds between exercises):
     - Rowing Machine
     - Jump Rope
     - Box Jumps
     - Battle Ropes
     - Burpees
     - Mountain Climbers
   - **Repeat** the circuit 3-4 times
   - **Cool-Down**: 5-10 minutes of stretching

**Additional Notes**

- **Variety**: Incorporate different machines or outdoor activities to engage various muscle groups.
- **Intensity**: Maintain a moderate to high intensity throughout the session.
"""
        ),
        TrainingPlan(
            week_number=1,
            day='Friday',
            exercise_details="""
**Warm-Up**

- **Dynamic Stretching** (Perform each exercise for 30 seconds to 1 minute):
  1. **Torso Twists**
  2. **Side Bends**
  3. **Arm Swings**
  4. **Hip Openers**

- **Light Cardio** (Choose one, 5-10 minutes):
  - **Option 1**: Light Jog Outside or on Treadmill
  - **Option 2**: Elliptical Machine
  - **Option 3**: Stationary Bike
  - **Option 4**: Stair Climber

- **Mobility Drills** (Perform 1-2 sets of 10 reps each):
  1. **Thoracic Spine Rotations**
  2. **World's Greatest Stretch**
  3. **Inchworms**

**Strength Training**

1. **Clean and Press**
   - 5 sets x 3 reps
2. **Farmer's Walk**
   - 3 sets x 40 meters
3. **Turkish Get-Ups**
   - 3 sets x 5 reps per side
4. **Medicine Ball Slams**
   - 3 sets x 10 reps
5. **Battle Ropes**
   - 3 sets x 30 seconds

**Core Work**

- **Windshield Wipers**
  - 3 sets x 10 reps per side
- **Side Planks**
  - 3 sets x 45 seconds per side

**Cool-Down**

- **Static Stretching**: Full-body focus
- **Breathing Exercises**: Promote relaxation and recovery
"""
        ),
        TrainingPlan(
            week_number=1,
            day='Saturday',
            exercise_details="""
**Endurance and Recovery**

Choose one:

**Option 1: Ruck March**

- **Distance**: 6 miles with a 35-pound pack
- **Terrain**: Varied (hills, trails, flats)
- **Focus**: Steady pace, maintaining good posture

**Option 2: Interval Running**

- **Warm-Up**: 10-minute easy jog
- **Workout**:
  - 6 x 400 meters at high intensity with 2-minute rest between
- **Cool-Down**: 10-minute walk or light jog

**Option 3: Swimming**

- **Distance**: 1,500 meters
- **Focus**: Steady pace, efficient technique

**Recovery Activities**

- **Yoga or Stretching Session**: 30 minutes focusing on flexibility
- **Hydrotherapy**: Contrast showers or ice baths to aid recovery
"""
        ),
        # Weeks 2 to 6 (You can add more detailed entries if needed)
    ]

    # Generate entries for weeks 2 to 6
    for week in range(2, 7):
        plan_items.extend([
            TrainingPlan(
                week_number=week,
                day='Monday',
                exercise_details=f"""
**Week {week} Monday: Upper Body Strength**

- Repeat Monday's routine with progressive overload.
- Increase weights by 2.5-5% if form permits.
- Focus on maintaining proper form and technique.
"""
            ),
            TrainingPlan(
                week_number=week,
                day='Tuesday',
                exercise_details=f"""
**Week {week} Tuesday: Strict Cardio**

- Repeat Tuesday's cardio session.
- Vary intensity or duration to continue challenging the body.
- Consider trying a different cardio option from previous weeks.
"""
            ),
            TrainingPlan(
                week_number=week,
                day='Wednesday',
                exercise_details=f"""
**Week {week} Wednesday: Lower Body Strength**

- Repeat Wednesday's routine with progressive overload.
- Increase weights or add an extra set/repetition.
- Ensure proper form to prevent injuries.
"""
            ),
            TrainingPlan(
                week_number=week,
                day='Thursday',
                exercise_details=f"""
**Week {week} Thursday: Strict Cardio**

- Repeat Thursday's cardio session.
- Introduce new interval patterns or increase distances.
- Maintain high intensity to improve cardiovascular fitness.
"""
            ),
            TrainingPlan(
                week_number=week,
                day='Friday',
                exercise_details=f"""
**Week {week} Friday: Full-Body Functional Strength**

- Repeat Friday's routine with progressive overload.
- Focus on improving technique in complex movements like the Clean and Press.
- Adjust weights and intensities as needed.
"""
            ),
            TrainingPlan(
                week_number=week,
                day='Saturday',
                exercise_details=f"""
**Week {week} Saturday: Endurance and Recovery**

- Repeat Saturday's endurance activities.
- Aim to improve times or distances from previous weeks.
- Continue incorporating recovery practices like yoga or hydrotherapy.
"""
            ),
        ])

    # Add all items to the session
    db.session.bulk_save_objects(plan_items)
    db.session.commit()
    print("Training plan populated successfully.")
