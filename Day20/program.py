import sys
import time
import re
import math

title = "## Day 20: Particle Swarm ##"
url = "https://adventofcode.com/2017/day/20"
expectedResultPart1 = 457
expectedResultPart2 = 448

class Particle:
    def __init__(self, id, p, v, a):
        self.p = p
        self.v = v
        self.a = a
        self.id = id
        self.px = int(p[0])
        self.py = int(p[1])
        self.pz = int(p[2])
        self.vx = int(v[0])
        self.vy = int(v[1])
        self.vz = int(v[2])
        self.ax = int(a[0])
        self.ay = int(a[1])
        self.az = int(a[2])
        self.is_destroyed = False
    
    def clone(self):
        return Particle(self.id, self.p, self.v, self.a)

    def move(self):
        self.vx += self.ax
        self.vy += self.ay
        self.vz += self.az
        self.px += self.vx
        self.py += self.vy
        self.pz += self.vz
        
    def distance_from(self, p):
        return abs(self.px - p.px) + abs(self.py - p.py) + abs(self.pz - p.pz)

    def distance_from_origin(self):
        return abs(self.px) + abs(self.py) + abs(self.pz)

def find_collision_time(p1, p2, max_time=50):
    for t in range(max_time + 1):
        p1.move()
        p2.move()
        if p1.distance_from(p2) == 0:
            return t
    return None   

def find_when_closest_to_origin(particle):
    min_dist = particle.distance_from_origin()
    while True:
        particle.move();
        if (particle.distance_from_origin() < min_dist):
            min_dist = particle.distance_from_origin()
            continue
        return min_dist

def get_particles(input):
    particles = []
    lines = input.splitlines()
    for idx, line in enumerate(lines):
        matches = re.findall(r'(-?\d+)', line)
        assert len(matches) == 9, f"Expected 9 matches, Found:{len(matches)}, Matches:{matches}"
        particle = Particle(idx, matches[:3], matches[3:6], matches[6:9])
        particles.append(particle)
    return particles

def partOne(input):
    particles = get_particles(input)

    # find min acceleration
    min_acceleration = sys.maxsize
    for p in particles:
        p_accel = abs(p.ax) + abs(p.ay) + abs(p.az)
        if p_accel < min_acceleration:
            min_acceleration = p_accel
    
    candidates = [] # particles with the min acceleration
    for idx, p in enumerate(particles):
        p_accel = abs(p.ax) + abs(p.ay) + abs(p.az)
        if p_accel == min_acceleration:
            candidates.append(idx)

    p_id = -1
    min_dist = sys.maxsize
    for id in candidates:
        p = particles[id]
        p_min_dist = find_when_closest_to_origin(p)
        p.move()
        dist_delta = p.distance_from_origin() - p_min_dist
        if (dist_delta < min_dist):
            min_dist = dist_delta
            p_id = id

    return p_id

def partTwo(input):
    particles = get_particles(input)
    prev_dist_apart = {}
    collisions = {}

    for i in range(len(particles) - 1):
        p1 = particles[i]
        for j in range(i + 1, len(particles)):
            p2 = particles[j]
            
            t = find_collision_time(p1.clone(), p2.clone())
            if t is not None:
                collisions[(p1.id, p2.id)] = t

    sorted_collisions = dict(sorted(collisions.items(), key=lambda item: item))

    for (p1_id, p2_id), ticks in sorted_collisions.items():
        p1 = particles[p1_id]
        p2 = particles[p2_id]
        if not p1.is_destroyed or not p2.is_destroyed:
            p1.is_destroyed = True
            p2.is_destroyed = True
    
    remaining = 0
    for p in particles:
        if not p.is_destroyed:
            remaining += 1
    
    return remaining

print(title)
print(url)
for filePath in sys.argv[1:]:
    print(f"\nFile: {filePath}")
    with open(filePath, 'r') as file:
        input = file.read()

    start = time.perf_counter()
    resultPartOne = partOne(input);
    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000
    print(f"Part 1 Result: {resultPartOne} in {elapsed_ms:.3f}ms");

    start = time.perf_counter()
    resultPartTwo = partTwo(input);
    end = time.perf_counter()
    elapsed_ms = (end - start) * 1000
    print(f"Part 2 Result: {resultPartTwo} in {elapsed_ms:.3f}ms");

if (resultPartOne != expectedResultPart1 or resultPartTwo != expectedResultPart2):
        sys.exit(1)
