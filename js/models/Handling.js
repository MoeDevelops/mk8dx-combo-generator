class Handling {
    constructor(ground, water, air, antiGravity){
        this.ground = ground;
        this.water = water;
        this.air = air;
        this.antiGravity = antiGravity;
    }

    total() {
        return this.ground + this.water + this.air + this.antiGravity;
    }
}