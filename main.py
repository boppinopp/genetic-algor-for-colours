import pygame
from random import randint,choices,random,choice
import numpy as np


#apply genetic algorthim 
# define genome 
# create fitness func and eval
# create next generation - crossover best people , keep the best , create chance for mutation 
# repeat until met condition - in my case eval func score of 0 - match colour perfectly 




class agent():
    def __init__(self,genome,x,y):
        self.genome = genome
        self.r = self.genome[0]
        self.g = self.genome[1]
        self.b = self.genome[2]
        
        self.body = pygame.rect.Rect(x,y,10,10)
        self.fitness_score = None
    
    def fitness_func(self,screen_colour):
        red_score = abs(screen_colour[0] - self.r)
        green_score =  abs(screen_colour[1] - self.g)
        blue_score = abs(screen_colour[2] - self.b)
        # the larger the total the worse 
        total = red_score + green_score + blue_score
        return total

def mutation(genome):
    mutation_chance = 0.01
    mutation_magnitude = 10
    new_genome = ()
    for gene in genome:
        
        if random() < mutation_chance:
            
            
            mutated_gene = choice((gene + mutation_magnitude, gene - mutation_magnitude))
            
            
            # check if vlaid for rgb range
            if mutated_gene >= 255:
                gene =  255
            elif mutated_gene <= 0:
                gene =  0 
            else:
                gene =  mutated_gene
        new_genome += (gene,)
     
    return new_genome
            


def crossing_over(top_population):
    # randomly pick from top 10%
    genome1,genome2 = choices(top_population,k=2)
    n = randint(1,2)

    new_genome1 = genome1.genome[:n] + genome2.genome[n:]
    new_genome2 = genome2.genome[:n] + genome1.genome[n:]

    # check if mutation occurs
    # each part of the genome can change, none , one or all at onec
    
    new_genome1 = mutation(new_genome1)
    new_genome2 = mutation(new_genome2)

    



    # create new agents with genome
    return(new_genome1,new_genome2)

    


pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("genetic algorthim for camoflauge")
screen_colour = (0,0,0)
population_size =3200
running  = True

steps = 0 
new_genomes =[]
genomes = []
for _ in range(population_size):
    genome = (randint(0,255),randint(0,255),randint(0,255))
    genomes.append(genome)

# need to geneerate (r,g,b )


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            running = False
    
    
    


    
    
    
    
    

    population = []
    new_genomes =[]
    new_population= []
    sum_fitness =[]
    genome_index = 0
    
   

    screen.fill(screen_colour)


    for y in range (400,800,10):
        for x in range (0,800,10):
            
            agent1 =agent(genomes[genome_index],x,y)
            population.append(agent1)
            pygame.draw.rect(screen,(agent1.r,agent1.g,agent1.b),agent1.body)
            # eval fitness 
            agent1.fitness_score = agent1.fitness_func(screen_colour)
            
            sum_fitness.append(agent1.fitness_score)
            genome_index+=1


            
    
        
                
    
    

        
    # sort population by lowest score
    population.sort(key= lambda x:x.fitness_score)
    top_population = population[:320]
    for person in top_population:
        new_genomes.append(person.genome)
    
    # need to make a new population of 3200 , take top 10% which makes 320 , then cross over the rest 
   
    while len(new_genomes) < population_size:
        omes = crossing_over(top_population)
        print(omes)
        new_genomes.extend(omes)
        

    genomes = new_genomes

    steps+=1
    print(steps)
    if steps == 100:
        screen_colour = (randint(0,255),randint(0,255),randint(0,255))
        steps = 0
        
    

    pygame.display.update()

pygame.quit()