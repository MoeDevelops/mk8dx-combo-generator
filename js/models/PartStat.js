class PartStat{
    constructor(speed, acceleration, weight, handling, traction, miniTurbo, invincibility){
        this.speed = speed;
        this.acceleration = acceleration;
        this.weight = weight;
        this.handling = handling;
        this.traction = traction;
        this.miniTurbo = miniTurbo;
        this.invincibility = invincibility;
    }

    total() {
        return this.speed.total() + this.acceleration + this.weight + this.handling.total() + this.traction + this.miniTurbo + this.invincibility;
    }
}